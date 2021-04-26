- nvidia is using Ansible to install k8s ( https://kubespray.io/#/ ): https://github.com/NVIDIA/deepops/tree/master/docs/k8s-cluster    

- and using Ansible to install Slurm : https://github.com/NVIDIA/deepops/tree/master/docs/slurm-cluster
#### Singularity can be installed by setting the slurm_cluster_install_singularity variable to yes before running the slurm-cluster.yml playbook.
