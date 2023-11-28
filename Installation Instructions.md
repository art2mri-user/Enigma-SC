# Installation Instructions

## 1) System Requirements  

- To install **enigma2** it is required at least 25 GB free space in your hard disk.  

- This software has been tested and works pretty well on the Ubuntu 20.04, Ubuntu 20.10, Ubuntu 22.04 and MacOS operating systems.

- The **enigma2** fundamentally runs its application on top of other tools, so it's necessary for the user to install the following applications:
  
  Python 3.11.5 - [Installation](https://www.python.org/downloads/)  
  SCT 5.8 (or more recent versions) - [Installation](https://spinalcordtoolbox.com/index.html)  
  Docker Engine - [Installation](https://docs.docker.com/engine/install/ubuntu/)  
  Singularity - [Installation](https://github.com/apptainer/singularity/blob/master/INSTALL.md)  

- We strongly reccomend the GPU integration for optimizing the prediction time of your results. However, inference times are typically still manageable on CPU and MPS (Apple M1/M2). If using a GPU, it should have at least 4 GB of available (unused) VRAM.    
  
  CUDA-toolkit - [Installation](https://developer.nvidia.com/cuda-toolkit-archive)  
  CUDA container-toolkit - [Installation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

## 2) Download and Install enigma2 

### Installing enigma2

To download and install enigma2, open a terminal and type:  
  
```bash
git clone https://github.com/art2mri/enigma2.git  
sudo chmod -R 777 enigma2/enigma2.sh
```   
 
 It will clone all the enigma2 repository files to an enigma2 folder that will be created in your computer. **NOTE: Please don't rename the enigma2 folder, you should keep it just like that. You can move the entire folder to any other locations, but never changing its name**.

 ### Installing virtual environment to run enigma2 

 Inside of the enigma2 folder, open a terminal and type the following commands:  

 ```bash
pip install virtualenv
```
 ```bash
sudo apt install python3-venv
```
 ```bash
python3.11 -m venv venv
```
 ```bash
source venv/bin/activate
```
 ```bash
pip install Pillow
```
 ```bash
pip3 install tkfilebrowser
```
### Running enigma2  

To run the **enigma2** software and open the interface, just open a terminal **inside of the enigma2 folder** and type:  

 ```bash
source venv/bin/activate  
./enigma2.sh
```
 
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

### Option 1  

To download and install enigma2, open a terminal and type:  
  
```bash
git clone https://github.com/art2mri/enigma2.git  
sudo chmod -R 777 enigma2/enigma2.sh
```   
 
 It will clone all the enigma2 repository files to an enigma2 folder that will be created in your computer. **NOTE: Please don't rename the enigma2 folder, you should keep it just like that. You can move the entire folder to any other locations, but never changing its name**. 

 ### Option 2  
 
Optionally, you may create a folder named **enigma2** somewhere in your computer, and [download all this files](../../archive/main.zip) inside of it, including the ***vertebral_labeling.simg*** folder you have created from the previous step, you should cut it and place inside of the **enigma2** folder. After that, open a terminal inside of the enigma2 folder and type: `sudo chmod -R 777 enigma2.sh'. **Just to remind you, after you downloaded the files and extracted it, a *enigma2-main* folder will be created, don't forget to rename it to *enigma2*.** You can place this enigma2 folder anywhere you want.  






  
   
  

  

  
