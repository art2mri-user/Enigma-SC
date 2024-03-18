## Command Line Tutorial

### Use this alternative only if you cannot install the GUI for some reason

To visualize the MENU, open a terminal inside of the **Enigma-SC** folder and type: `./nographmode.sh` 

!["nographmode MENU"](img/command1.png)  

The user should follow the numeric sequence of the numbers in green **(1 - 2 - 3 - 5 - 7 - 8)**. The numbers in yellow (4 and 6) only must be triggered in special ocasions (number 4 and 6 only for those images which failed on step number 3 and 5) and number 9 (to open this tutorial page).  


### 1. Prepare Folders  

Before typing this option, the user should create an **output** folder (you can choose any name, without spaces) where all the files generated on the following steps will be placed in. The **input** folder must have all the .nii.gz files you want to process (only the .nii.gz files) and they will be selected automatically. Your **input** folder can be also a BIDS dataset (all the anatomical data name must end with T1w.nii.gz, for example: sub-01_T1w.nii.gz or sub-02_T1w.nii.gz)  

After type 1 on the terminal, the user will be asked to choose the input files option (.nii.gz or BIDS). After the choice, the path of the **output** folder will be asked, and the entire path must be given, for example: **/home/art2mri/Documents/output** If you don't know how to find the path, open a terminal inside of the output folder and type **pwd**.  
