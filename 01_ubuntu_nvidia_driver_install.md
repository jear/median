```
sudo apt install gcc make 
sudo vi /etc/netplan/00-installer-config.yaml 
sudo netplan apply
sudo bash -c "echo blacklist nouveau > /etc/modprobe.d/blacklist-nvidia-nouveau.conf"sudo bash -c "echo blacklist nouveau > /etc/modprobe.d/blacklist-nvidia-nouveau.conf"
sudo bash -c "echo options nouveau modeset=0 >> /etc/modprobe.d/blacklist-nvidia-nouveau.conf"
cat /etc/modprobe.d/blacklist-nvidia-nouveau.conf
update-initramfs -u 
reboot


BASE_URL=https://us.download.nvidia.com/tesla
# DRIVER_VERSION=450.80.02
DRIVER_VERSION=460.32.03
curl -fSsl -O $BASE_URL/$DRIVER_VERSION/NVIDIA-Linux-x86_64-$DRIVER_VERSION.run
chmod +x NVIDIA-Linux-x86_64-460.32.03.run 
sudo ./NVIDIA-Linux-x86_64-460.32.03.run 
``` 
