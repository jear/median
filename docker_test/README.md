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
## Anaconda Docker image
```
docker build -t camera-seg .
```
