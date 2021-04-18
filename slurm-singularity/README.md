## Example GENCI / IDRIS
http://www.idris.fr/jean-zay/cpu/jean-zay-utilisation-singularity.html

Below is an example of SLURM batch script to execute TensorFlow within Singularity to train the CIFAR-10 model on a single GPU. The example also makes use of the local SSD ($LSTOR) available on the compute nodes to speed up processing of all the small images.


```
#!/bin/bash
#SBATCH --job-name=SingularityGPU      # nom du job
##SBATCH --partition=gpu_p2            # de-commente pour la partition gpu_p2
#SBATCH --ntasks=1                     # nombre total de taches (= nombre de GPU ici)
#SBATCH --gres=gpu:1                   # nombre de GPU per noeud (1/4 des GPU)
#SBATCH --cpus-per-task=10             # nombre de coeurs CPU par tache (1/4 du noeud 4-GPU)
##SBATCH --cpus-per-task=3             # nombre de coeurs CPU par tache (pour gpu_p2 : 1/8 du noeud 8-GPU)
# /!\ Attention, "multithread" fait reference a  l'hyperthreading dans la terminologie Slurm
#SBATCH --hint=nomultithread           # hyperthreading desactive
#SBATCH --time=00:10:00                # Temps d'execution maximum demande (HH:MM:SS)
#SBATCH --output=SingularityGPU%j.out  # Nom du fichier de sortie
#SBATCH --error=SingularityGPU%j.out   # Nom du fichier d'erreur (ici commun avec la sortie)

# on se place dans le repertoire de soumission
cd ${SLURM_SUBMIT_DIR}

# nettoyage des modules charges en interactif et herites par defaut
module purge

# chargement des modules
module load singularity

# echo des commandes lancees
set -x

# execution du code depuis espace d'execution autorise avec l'option --nv afin de prendre en compte les cartes NVIDIA
srun singularity exec --nv $SINGULARITY_ALLOWED_DIR/my-container_GPU.sif python ./my_model.py
```

## examples
https://qywu.github.io/2020/12/09/aws-slumr-pytorch.html

## another one
https://xstream.stanford.edu/docs/singularity/
```
#!/bin/bash
#SBATCH --job-name=cifar10_1gpu
#SBATCH --output=slurm_cifar10_1gpu_%j.out
#SBATCH --cpus-per-task=1
#SBATCH --gres gpu:1
#SBATCH --time=1:00:00

TF_IMG=tensorflow-latest-gpu.img
CIFAR10_DIR=$WORK/tensorflow/cifar10

mkdir $LSTOR/cifar10_data
cp -v cifar-10-binary.tar.gz $LSTOR/cifar10_data/

module load singularity

srun singularity exec --home $WORK:/home --bind $LSTOR:/tmp --nv $TF_IMG \
    python $CIFAR10_DIR/cifar10_train.py --batch_size=128 \
                                         --max_steps=100000
```
