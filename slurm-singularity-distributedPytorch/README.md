WORK IN PROGRESS


https://github.com/pytorch/pytorch/tree/master/torch/distributed/benchmarks

## Slurm + Singularity + distributed pytorch ( 2 GPU )
First, prepare a Dockerfile. We will use the pre-built docker containers from NGC (Nvidia GPU Cloud) as a starting point.
```
FROM nvcr.io/nvidia/pytorch:20.11-py3

# Install necessary packages
RUN apt-get update && \
    apt-get install -y vim git sudo wget

# Setup new user and sudo permission
RUN adduser --disabled-password --gecos '' ubuntu && \
    adduser ubuntu sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Setup colorful prompt
RUN sed -i 's/#force_color_prompt=yes/force_color_prompt=yes/g' /home/ubuntu/.bashrc

# Get into the user directory
USER ubuntu
WORKDIR /home/ubuntu

# Initialize anaconda
RUN /opt/conda/bin/conda init

```

After you have created the Dockerfile, build it into a new image named torch, and run a container based on the new image.
```
docker build -t torch .
docker run --gpus all --rm torch nvidia-smi
```
Next, we can convert the image we just built into a Singularity image.
```
sudo singularity build torch.simg docker-daemon://torch:latest
```
After about 10 minutes, you should see a file torch.simg in the current working directory. Let’s run it.
```
singularity shell --nv torch.simg
```
Finally, you have set up a singularity container that is ready for the cluster training.

## PyTorch Distributed Training

This part shows how distributed training works on PyTorch. Here is an example code for running MNIST classification task.
```
import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.distributed as dist
from torch.distributed import get_rank
from torchvision import datasets, transforms

# pylint:disable=no-member


class Hyperparams:
    random_seed = 123
    batch_size = 32
    test_batch_size = 32
    lr = 1e-3
    epochs = 10
    save_model = False
    log_interval = 100
    num_gpus_per_node = 2
    num_nodes = 1


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1)
        self.dropout1 = nn.Dropout(0.25)
        self.dropout2 = nn.Dropout(0.5)
        self.fc1 = nn.Linear(9216, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output


def train(args, model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()

        if Hyperparams.rank == 0 and batch_idx % args.log_interval == 0:
            print(
                'Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                    epoch, batch_idx * len(data), len(train_loader.dataset), 100. * batch_idx / len(train_loader),
                    loss.item()
                )
            )


def test(model, device, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            test_loss += F.nll_loss(output, target, reduction='sum').item()  # sum up batch loss
            pred = output.argmax(dim=1, keepdim=True)  # get the index of the max log-probability
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)

    print(
        '\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
            test_loss, correct, len(test_loader.dataset), 100. * correct / len(test_loader.dataset)
        )
    )


def main():
    # torch.manual_seed(Hyperparams.random_seed)

    local_rank = int(os.environ.get("LOCAL_RANK", 0))
    rank = int(os.environ.get("RANK", 0))
    Hyperparams.rank = rank
    world_size = int(os.environ.get("WORLD_SIZE", 1))
    num_gpus_per_node = max(rank - local_rank, world_size)
    num_nodes = world_size // num_gpus_per_node

    if world_size > 1:
        torch.cuda.set_device(local_rank)
        dist.init_process_group(backend="nccl", init_method='env://')
        node_rank = rank // num_gpus_per_node
        print(f"Initialized Rank:{dist.get_rank()} on Node Rank:{node_rank}")

    device = torch.device("cuda")

    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307, ), (0.3081, ))])

    if rank == 0:
        dataset1 = datasets.MNIST('../data', train=True, download=True, transform=transform)
        if world_size > 1:
            dist.barrier()
    else:
        if world_size > 1:
            dist.barrier()
        dataset1 = datasets.MNIST('../data', train=True, download=False, transform=transform)

    dataset2 = datasets.MNIST('../data', train=False, transform=transform)

    train_loader = torch.utils.data.DataLoader(dataset1, batch_size=Hyperparams.batch_size, shuffle=True)
    test_loader = torch.utils.data.DataLoader(dataset2, batch_size=Hyperparams.test_batch_size)

    model = Net().to(device)

    if world_size > 1:
        model = nn.parallel.DistributedDataParallel(model, device_ids=[local_rank], output_device=local_rank)

    optimizer = optim.AdamW(model.parameters(), lr=Hyperparams.lr)

    for epoch in range(1, Hyperparams.epochs + 1):
        train(Hyperparams, model, device, train_loader, optimizer, epoch)
        if rank == 0:
            test(model, device, test_loader)

    if rank == 0 and Hyperparams.save_model:
        torch.save(model.state_dict(), "mnist_cnn.pt")


if __name__ == "__main__":
    main()
```

We will take advantage of a utility script torch.distributed.launch in the PyTorch repository.
- https://github.com/pytorch/pytorch/blob/master/torch/distributed/launch.py


Source :
- https://qywu.github.io/2020/12/09/aws-slumr-pytorch.html

