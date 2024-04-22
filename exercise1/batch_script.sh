#!/bin/bash -l
#SBATCH -J hello_worl_OpenMPd
#SBATCH -t 00:10:00
#SBATCH -A edu24.DD2356
#SBATCH --nodes=1
#SBATCH -p main
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=64
#SBATCH -o hello_world_OpenMP%j.out 
#SBATCH -e hello_world_OpenMP%j.err 
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun -n 1 ./hello_world
