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



Source :
- https://qywu.github.io/2020/12/09/aws-slumr-pytorch.html

