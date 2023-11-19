# Installation Instructions

## 1) System Requirements  

- This software has been tested and achieves its best performance on the Ubuntu 20.04, Ubuntu 20.10, Ubuntu 22.04 and MacOS operating systems.

- The **enigma2** fundamentally runs its application on top of other tools, so it's necessary for the user to install the following applications:
  
  Python 3.10.12 (or more recent versions) - [Installation](https://www.python.org/downloads/)  
  SCT 5.8 (or more recent versions) - [Installation](https://spinalcordtoolbox.com/index.html)  
  Docker Engine - [Installation](https://docs.docker.com/engine/install/ubuntu/)  
  Singularity - [Installation](https://github.com/apptainer/singularity/blob/master/INSTALL.md)  

- We strongly reccomend the GPU integration for optimizing the prediction time of your results. However, inference times are typically still manageable on CPU and MPS (Apple M1/M2). If using a GPU, it should have at least 4 GB of available (unused) VRAM.    
  
  CUDA-toolkit - [Installation](https://developer.nvidia.com/cuda-toolkit-archive)  
  CUDA container-toolkit - [Installation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

## 2) Updating Packages  

- Run the following commands on Linux Terminal to install all packages dependencies:

  - `pip install Pillow` or `pip3 install Pillow` or if you already have it installed, just run `pip install --upgrade Pillow`
  - `sudo apt-get install python3-tk` or `pip3 install tkfilebrowser`

 
## 3) Docker and Singularity Containers  

- You don't necessarily need to install both of these applications; you can choose to install just one of them to run the spinal cord vertebral labeling (if you prefer). The containers will be automatically initialized from an existing Docker image that is already available on [DockerHub](https://hub.docker.com/repository/docker/art2mri/vertebral_labeling/general).

  ### Docker
  
  If you have already correctly installed the Docker Engine, just run the following command on Linux Terminal:
   - `sudo docker pull art2mri/vertebral_labeling:1.0`

  ### Singularity

  If you have correctly installed the Singularity, just open the Linux terminal in the same path where you have installed it run the following command:
  - `sudo singularity build --sandbox vertebral_labeling.simg docker://art2mri/vertebral_labeling:1.0`
  - After that, a folder named ***vertebral_labeling.simg*** will appear on the Singularity folder.
  - Run the following command on the terminal: `sudo chmod -R 777 vertebral_labeling.simg` to avoid any permission related problems.   
 
## 4) Download and Install enigma2  

To download and install enigma2, open a terminal and type:  
  
```bash
git clone https://github.com/art2mri/enigma2.git&&sudo chmod -R 777 enigma2/enigma2.sh
```   
 
 It will clone all the enigma2 repository files to an enigma2 folder that will be created in your computer. **NOTE: Please don't rename the enigma2 folder, you should keep it just like that. Tou can move the entire folder to any other locations, but never changing its name**. 

Now, all you have to do is to create a folder named **enigma2** somewhere in your computer, and [download all this files](../../archive/main.zip) inside of it, including the ***vertebral_labeling.simg*** folder you have created from the previous step, you should cut it and place inside of the **enigma2** folder. 

Just to remind you, after you downloaded files and extracted it, a *enigma2-main* folder will be created, don't forget to rename it to *enigma2*. You can place this folder anywhere you want.

  
   
  

  

  
