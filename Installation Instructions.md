# Installation Instructions

## 1) System Requirements  

- To install **Enigma-SC** it is required at least 25 GB free space in your hard disk.  

- This software has been tested on Ubuntu 20.04, Ubuntu 20.10 and Ubuntu 22.04.

- The **Enigma-SC** fundamentally runs its application on top of other tools, so it's necessary for the user to install the following applications:
  
  Python 3.11.5 - [Installation](https://www.python.org/downloads/)  
  SCT - [Installation](https://spinalcordtoolbox.com/index.html)  
  Docker Engine - [Installation](https://docs.docker.com/engine/install/ubuntu/)  
  Singularity - [Installation](https://github.com/apptainer/singularity/blob/master/INSTALL.md)  

- We strongly reccomend the GPU integration for optimizing the prediction time of your results. However, inference times are typically still manageable on CPU and MPS (Apple M1/M2). If using a GPU, it should have at least 4 GB of available (unused) VRAM.    
  
  CUDA-toolkit - [Installation](https://developer.nvidia.com/cuda-toolkit-archive)  
  CUDA container-toolkit - [Installation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

  Once you have installed the CUDA, open a terminal and type `nvidia-smi` to check if it was correctly installed.  
  
## 2) Download and Install Enigma-SC 

### Installing Enigma-SC

To download and install Enigma-SC, open a terminal and type:  
  
```bash
git clone https://github.com/art2mri/Enigma-SC.git  
sudo chmod -R 777 Enigma-SC/Enigma-SC.sh
```   
 
 It will clone all the Enigma-SC repository files to an Enigma-SC folder that will be created in your computer. **NOTE: Please don't rename the Enigma-SC folder, you should keep it just like that. You can move the entire folder to any other locations, but never changing its name**.

 ### Installing virtual environment to run Enigma-SC 

 Inside of the **Enigma-SC** folder, open a terminal and type the following commands:  

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
### Running Enigma-SC  

To run the **Enigma-SC** software and open the interface, just open a terminal **inside of the Enigma-SC folder** and type:  

 ```bash
source venv/bin/activate  
./Enigma-SC.sh
```
 
## 3) Docker and Singularity Containers  

- You don't necessarily need to install both of these applications; you can choose to install just one of them to run the spinal cord vertebral labeling (if you prefer). The containers will be automatically initialized from an existing Docker image that is already available on [DockerHub](https://hub.docker.com/repository/docker/art2mri/vertebral_labeling/general).

  ### Docker
  
  If you have already correctly installed the Docker Engine, just run the following command on Linux Terminal:
   - ```bash
     sudo docker pull art2mri/vertebral_labeling:3.0
     ```
     
  ### Singularity

  If you have correctly installed the Singularity, just open the Linux terminal **inside of the Enigma-SC folder** and run the following command:
  - ```bash
    sudo singularity build --sandbox vertebral_labeling.simg docker://art2mri/vertebral_labeling:3.0
    ```
  - ```bash
    sudo chmod -R 777 vertebral_labeling.simg
    ```  
  - After that, a folder named ***vertebral_labeling.simg*** will appear on the **Enigma-SC** folder. PLease don't rename it.
 
## 4) Uninstalling Enigma-SC     
 






  
   
  

  

  
