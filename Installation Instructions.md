# Installation Instructions

**1) System Requirements**  

- This software has been tested and achieves its best performance on the Ubuntu 20.04, Ubuntu 20.10, Ubuntu 22.04 and MacOS operating systems.

- The **enigma2** fundamentally runs its application on top of other tools, so it's necessary for the user to install the following applications:
  
  Python 3.10.12 (or more recent versions) - [Installation](https://www.python.org/downloads/)  
  SCT 5.8 (or more recent versions) - [Installation](https://spinalcordtoolbox.com/index.html)  
  Docker Engine - [Installation](https://docs.docker.com/engine/install/ubuntu/)  
  Singularity - [Installation](https://github.com/apptainer/singularity/blob/master/INSTALL.md)  

- We strongly reccomend the GPU integration for optimizing the prediction time of your results. However, inference times are typically still manageable on CPU and MPS (Apple M1/M2). If using a GPU, it should have at least 4 GB of available (unused) VRAM.    
  
  CUDA-toolkit - [Installation](https://developer.nvidia.com/cuda-toolkit-archive)  
  CUDA container-toolkit - [Installation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

**2) Updating Packages**  

- Run the following commands on Linux Terminal to install all packages dependencies:

  `pip install Pillow` or `pip3 install Pillow` or if you already have it installed, just run `pip install --upgrade Pillow`

  

  
