## Install nvidia-docker
Source: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#nvidia-drivers
```
cat /etc/docker/daemon.json 
{
    "default-runtime": "nvidia",
    "runtimes": {
        "nvidia": {
            "path": "nvidia-container-runtime",
            "runtimeArgs": []
        }
    }
}
```

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


...



 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.24894
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.42059
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.25627
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.07379
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.26865
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.40180
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.23537
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.34204
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.35817
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.11574
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.39158
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.55408
Current AP: 0.24894
DLL 2021-04-20 11:16:48.691423 - (64,) mAP : 0.24894283339490403 
DLL 2021-04-20 11:16:48.691518 - () total time : 44247.04624032974 
DLL 2021-04-20 11:16:48.691536 - () mAP : 0.24894283339490403 

12 hours on a DL380 with 1 A100 40GB 

```
