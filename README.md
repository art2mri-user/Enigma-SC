# enigma2
An optimized deep learning-based method for spinal cord vertebral labeling.

# What is enigma2 ?

# How does the enigma2 work ?

# Getting started

Read these before you start:  
[Installation Instructions](/Installation%20Instructions.md)

!["enigma2 interface"](interface.png)

**1) Running enigma2** 

Create a folder named **enigma2** somewhere in your computer and place all the files of enigma2 inside of it just like in the [Installation Instructions](/Installation%20Instructions.md).     

To see how to create the **vertebral_labeling.simg** folder correctly, please read the [Installation Instructions](/Installation%20Instructions.md). It will only be necessary if you want to run the predictions via the [Singularity Platform](https://singularity-userdoc.readthedocs.io/en/latest/).

To open the **enigma2** interface, open a terminal inside of the **enigma2** folder and type `./enigma2.sh`. Please don't forget to check if you have correctly installed all the requirements listed on [Installation Instructions](/Installation%20Instructions.md) before you run it.

**2) Prepare Folders** 

The first thing the user should do is to create a folder named **input** somewhere and place all desired .nii.gz files inside this folder so that the following steps can be performed. 

The Prepare Folder buttons takes all the files inside of the **input** folder, and divide them into differents subfolders into the **spine** folder which is created automatically outside of the **input** folder.
 

