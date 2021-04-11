## From Pytorch
Source : https://github.com/pytorch/pytorch/tree/master/docker/pytorch/ubuntu_cpu_gpu

```
# For example, for a CUDA 10.2 Ubuntu 18.04 and Python 3.9.1 build:
nvidia-docker build -t ubuntu_1804_py_39_cuda_102_cudnn_8_dev \
   --build-arg BASE_IMAGE=nvidia/cuda:10.2-cudnn8-devel-ubuntu18.04 \
   --build-arg PYTHON_VERSION=3.9.1 \
   --build-arg MAGMA_CUDA_VERSION=magma-cuda102 \
   --build-arg TORCH_CUDA_ARCH_LIST_VAR="3.7+PTX;5.0;6.0;6.1;7.0;7.5" .
```
