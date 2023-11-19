Install Python3.10.12 (or more recent versions) - https://www.python.org/downloads/
Install SCT 5.8 (or more recent versions) - https://spinalcordtoolbox.com/
Install Docker Engine - https://docs.docker.com/engine/install/ubuntu/
Install Singularity - https://github.com/apptainer/singularity/blob/master/INSTALL.md
Install CUDA-toolkit and CUDA container-toolkit

Run the following commands on Linux Terminal:

1) pip install Pillow
2) pip install --upgrade Pillow
3) sudo apt-get install python3-tk
4) pip3 install tkfilebrowser
5) sudo singularity build --sandbox vertebral_labeling.simg docker://art2mri/vertebral_labeling:1.0
6) sudo chmod -R 777 vertebral_labeling.simg
