import torch

batch_size = 8
n_batches = 100

tmp = 2*(torch.rand(n_batches, batch_size, 1, 8, 8)>0.5).float()-1.
GT = torch.stack([torch.nn.functional.interpolate(x, size=(512,512)) for x in tmp])
data = GT + 2*torch.rand(n_batches, batch_size, 1, 512, 512)-1
dataloader = [{"data": data[i], "GT": GT[i]} for i in range(n_batches)]

model = torch.hub.load('mateuszbuda/brain-segmentation-pytorch', 'unet',
    in_channels=1, out_channels=1, init_features=32, pretrained=False)
model.cuda()
model = torch.nn.DataParallel(model, device_ids=[0,1])

def loss(pred, GT):
    res = (pred-GT)**2
    res = res.mean()
    return res

optimizer = torch.optim.Adam(model.parameters(), lr=0.00003)

for epoch in range(5):
    costs = list()
    for sample in dataloader:
        optimizer.zero_grad()
        output = model(sample["data"].cuda())
        cost = loss(output, sample["GT"].cuda())
        costs.append(cost.item())
        cost.backward()
        optimizer.step()
    mean_cost = sum(costs)/len(costs)
    print("Loss:", int(1000*mean_cost)/1000)

print("Successful!")
