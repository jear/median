## From Nvidia 
Source : https://github.com/NVIDIA/DeepLearningExamples/tree/master/PyTorch/Detection/SSD#training-performance-benchmark
```
nvidia-docker run --rm -it --ulimit memlock=-1 --ulimit stack=67108864 -v $COCO_DIR:/coco --ipc=host nvidia_ssd

root@c534caf35cf4:/workspace# bash ./examples/SSD300_FP32_1GPU.sh . /coco
DLL 2021-04-10 08:50:05.114827 - PARAMETER dataset path : /coco  epochs : 65  batch size : 32  eval batch size : 32  no cuda : False  seed : None  checkpoint path : None  mode : training  eval on epochs : [21, 31, 37, 42, 48, 53, 59, 64]  lr decay epochs : [43, 54]  learning rate : 0.0026  momentum : 0.9  weight decay : 0.0005  lr warmup : 300  backbone : resnet50  backbone path : None  num workers : 4  AMP : False  precision : fp32
Using seed = 7224
loading annotations into memory...
Done (t=0.64s)
creating index...
index created!
```
