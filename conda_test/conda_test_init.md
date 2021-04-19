## Install Anaconda
```
jear@worker-gpu-7:~$ wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
jear@worker-gpu-7:~$ bash Anaconda3-2020.11-Linux-x86_64.sh

logout/login
```
 

## Create a python 3.6 venv
```
(base) jear@worker-gpu-7:~$ conda create --name py36-cuda10.2 python=3.6
```
 

## Activate
```
(base) jear@worker-gpu-7:~$ conda activate py36-cuda10.2
```
 

## Install cuda toolkit and pytorch
```
(py36-cuda10.2) jear@worker-gpu-7:~$ conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch
```
Test #1 :
```
(py36-cuda10.2) jear@worker-gpu-7:~$ python
Python 3.6.13 |Anaconda, Inc.| (default, Feb 23 2021, 21:15:04)
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.cuda.device_count()
1
>>> torch.cuda.is_available()
True
>>> print(torch.__version__)
1.8.1
>>>
```
 

## Deactivate
Test #2 : 
```
(base) jear@worker-gpu-7:~$ python
Python 3.8.5 (default, Sep  4 2020, 07:30:14)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'torch'

 
