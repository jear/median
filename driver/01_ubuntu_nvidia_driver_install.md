Install ubuntu 20.04 LTS :
- HWE 
- kernel param : nomodeset fsck.mode=skip pci=realloc=off
- openssh server

- https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html
- https://docs.nvidia.com/datacenter/tesla/hgx-software-guide/index.html


```
/!\  Warning, do not install nvidia driver, do not blacklist nouveau... the following will do it for you.

distribution=$(. /etc/os-release;echo $ID$VERSION_ID | sed -e 's/\.//g') && wget https://developer.download.nvidia.com/compute/cuda/repos/$distribution/x86_64/cuda-$distribution.pin && sudo mv cuda-$distribution.pin /etc/apt/preferences.d/cuda-repository-pin-600
 sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/$distribution/x86_64/7fa2af80.pub && echo "deb http://developer.download.nvidia.com/compute/cuda/repos/$distribution/x86_64 /" | sudo tee /etc/apt/sources.list.d/cuda.list && sudo apt-get update

sudo apt-cache madison cuda-drivers-fabricmanager-450
cuda-drivers-fabricmanager-450 | 450.102.04-1 | http://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
cuda-drivers-fabricmanager-450 | 450.102.04-1 | http://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
cuda-drivers-fabricmanager-450 | 450.80.02-1 | http://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
cuda-drivers-fabricmanager-450 | 450.80.02-1 | http://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
cuda-drivers-fabricmanager-450 | 450.51.06-1 | http://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages
cuda-drivers-fabricmanager-450 | 450.51.06-1 | http://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64  Packages

 
sudo apt-get install -y cuda-drivers-fabricmanager-450
 
nvidia-smi 
 
sudo reboot
 
 

 nvidia-smi topo -m
 /usr/bin/nv-fabricmanager --version
 Fabric Manager version is : 450.102.04

 sudo systemctl status nvidia-fabricmanager.service
 sudo systemctl start nvidia-fabricmanager.service
 sudo systemctl status nvidia-fabricmanager.service
 sudo apt-get install -y libnvidia-nscq-450
 ls -ol /usr/lib/x86_64-linux-gnu/libnvidia-nscq*
  
jear@worker-gpu-7:~$ sudo ls -l /dev/nv*
crw-rw-rw- 1 root root 195, 254 Apr 17 19:44 /dev/nvidia-modeset
crw-rw-rw- 1 root root 237, 255 Apr 17 19:45 /dev/nvidia-nvswitchctl
crw-rw-rw- 1 root root 236,   0 Apr 17 19:44 /dev/nvidia-uvm
crw-rw-rw- 1 root root 236,   1 Apr 17 19:44 /dev/nvidia-uvm-tools
crw-rw-rw- 1 root root 195,   0 Apr 17 19:44 /dev/nvidia0
crw-rw-rw- 1 root root 195, 255 Apr 17 19:44 /dev/nvidiactl
crw------- 1 root root  10, 144 Apr 17 19:44 /dev/nvram

/dev/nvidia-caps:
total 0
cr-------- 1 root root 239, 1 Apr 17 19:44 nvidia-cap1
cr--r--r-- 1 root root 239, 2 Apr 17 19:44 nvidia-cap2

jear@worker-gpu-7:~$ sudo nvidia-
nvidia-bug-report.sh     nvidia-cuda-mps-server   nvidia-modprobe          nvidia-settings          nvidia-xconfig           
nvidia-cuda-mps-control  nvidia-debugdump         nvidia-persistenced      nvidia-smi               


jear@worker-gpu-7:~$ nv
nv-fabricmanager         nvidia-cuda-mps-control  nvidia-debugdump         nvidia-persistenced      nvidia-smi               nvswitch-audit
nvidia-bug-report.sh     nvidia-cuda-mps-server   nvidia-modprobe          nvidia-settings          nvidia-xconfig           


``` 
