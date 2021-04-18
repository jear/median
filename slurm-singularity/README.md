## Example GENCI / IDRIS
http://www.idris.fr/jean-zay/cpu/jean-zay-utilisation-singularity.html
```
#!/bin/bash
#SBATCH --job-name=SingularityGPU      # nom du job
##SBATCH --partition=gpu_p2            # de-commente pour la partition gpu_p2
#SBATCH --ntasks=1                     # nombre total de taches (= nombre de GPU ici)
#SBATCH --gres=gpu:1                   # nombre de GPU per nÅ“ud (1/4 des GPU)
#SBATCH --cpus-per-task=10             # nombre de coeurs CPU par tache (1/4 du noeud 4-GPU)
##SBATCH --cpus-per-task=3             # nombre de coeurs CPU par tache (pour gpu_p2 : 1/8 du noeud 8-GPU)
# /!\ Attention, "multithread" fait reference Ã  l'hyperthreading dans la terminologie Slurm
#SBATCH --hint=nomultithread           # hyperthreading desactive
#SBATCH --time=00:10:00                # Temps dâ€™exÃ©cution maximum demande (HH:MM:SS)
#SBATCH --output=SingularityGPU%j.out  # Nom du fichier de sortie
#SBATCH --error=SingularityGPU%j.out   # Nom du fichier d'erreur (ici commun avec la sortie)

# on se place dans le rÃ©pertoire de soumission
cd ${SLURM_SUBMIT_DIR}

# nettoyage des modules charges en interactif et herites par defaut
module purge

# chargement des modules
module load singularity

# echo des commandes lancÃ©es
set -x

# exÃ©cution du code depuis espace dâ€™exÃ©cution autorisÃ© avec l'option --nv afin de prendre en compte les cartes NVIDIA
srun singularity exec --nv $SINGULARITY_ALLOWED_DIR/my-container_GPU.sif python ./my_model.py```

## Other examples
https://qywu.github.io/2020/12/09/aws-slumr-pytorch.html
