'''
BSD 3-Clause License

Copyright (c) 2023, art2mri

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''

import os
import subprocess
import csv
import math
import shutil
import getpass
import webbrowser
#from PIL import Image, ImageTk
from datetime import datetime


#############################

def get_pass():
	password = getpass.getpass('Enter the [sudo] password:')
	wrap = "sudo -S ls"
	try:
		subprocess.run(wrap, shell=True, check=True, input=password.encode(),stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	except subprocess.CalledProcessError as e:
		print("\033[91m\033[1mIncorrect password. Please try again.\033[0m")
		password = getpass.getpass('Enter the [sudo] password:')
	try:
		subprocess.run(wrap, shell=True, check=True, input=password.encode(),stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	except subprocess.CalledProcessError as e:
		print("\033[91m\033[1mIncorrect password. Aborting Function.\033[0m")
		raise SystemExit(1)
	return password
	
#############################

def get_exit(command_a, command_b):
		exit2 = subprocess.run(command_a, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
		if exit2 != 0:
			subprocess.run(command_b, shell=True, check=True)
		else:
			subprocess.run(command_a, shell=True, check=True)
			
#############################
def browse_folder_niigz():
	
	print('\033[94m\033[1mPLEASE TYPE THE PATH OF THE\033[0m \033[92m\033[1mOUTPUT\033[0m \033[94m\033[1mFOLDER\033[0m')
	output = input("output path: ")
	if not output:
		print('\033[91m\033[1mNo folder selected.\033[0m')
		return
	print ('\033[92m\033[1mSelected Folder:\033[0m')
	print(str(output))	
	print('\033[94m\033[1mNOW TYPE THE PATH OF THE\033[0m \033[92m\033[1m.nii.gz FILES\033[0m \033[94m\033[1mFOLDER:\033[0m')
	file_paths = input("input path: ")
	if not file_paths:
		print('\033[91m\033[1mNo folder selected.\033[0m')
		return		
	print ('\033[92m\033[1mSelected Files:\033[0m')
	path = str(file_paths)
	dir_list = os.listdir(path)
	for i in dir_list:
		print(str(i))
		
	before = str(file_paths)	
	output = str(output)
	
	for i in dir_list:
		if '.nii.gz' not in i:
			os.system(str(i)+'\033[91m\033[1m is not a .nii.gz file\033[0m')
		if '.nii.gz' in i:
			os.system('cd '+output+' && mkdir '+str(i).replace(".nii.gz",""))
			os.system('cp '+before+'/'+str(i)+' '+output+'/'+str(i).replace(".nii.gz",""))	
	print('\n')
	print('\033[92m\033[1mRESULTS:\033[0m')
	print('\n')	
	def check_subfolders(directory, output_file_path):
		all_responses_are_one = True
		with open(output_file_path, 'w') as output_file:
			for subfolder in os.listdir(directory):
				subfolder_path = os.path.join(directory, subfolder)
				if os.path.isdir(subfolder_path):
					files = os.listdir(subfolder_path)
					if any('.nii.gz' in file for file in files):
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[92m\033[1mOK\033[0m")
						output_file.write(f"{subfolder}.nii.gz OK" + '\n')						
					elif not os.listdir(subfolder_path):
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}\033[0m \033[93m\033[1mEMPTY FOLDER\033[0m")
						output_file.write(f"{subfolder}.nii.gz EMPTY FOLDER" + '\n')						
					else:
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[91m\033[1mFAILED (MISSING SEGMENTATION FILE)\033[0m")
						output_file.write(f"{subfolder}.nii.gz FAILED (MISSING SEGMENTATION FILE)" + '\n')
                			
		if all_responses_are_one:
			print('\n')
			print("\033[92m\033[1mFOLDERS PREPARED!\033[0m")
		else:
			print('\n')
			print("\033[93m\033[1mFOLDERS PREPARED - CHECK THE WARNINGS\033[0m")
	
	if not os.listdir(before):
		print('\n')
		print("\033[91m\033[1mPREPARING FOLDERS FAILED\033[0m")
	else:	      			
		check_subfolders(str(output), str(output)+'/PrepareFoldersResults.txt')	   							
					
	
	
#############################

def browse_folder_BIDS():

	print('\033[94m\033[1mPLEASE TYPE THE PATH OF THE\033[0m \033[92m\033[1mOUTPUT\033[0m \033[94m\033[1mFOLDER\033[0m')
	output = input("output path: ")
	if not output:
		print('\033[91m\033[1mNo folder selected.\033[0m')
		return
	print ('\033[92m\033[1mSelected Folder:\033[0m')
	print(str(output))	
	print('\033[94m\033[1mNOW TYPE THE PATH OF THE BIDS\033[0m \033[92m\033[1mDATASET\033[0m \033[94m\033[1mFOLDER:\033[0m')
	file_paths = input("BIDS dataset path: ")
	if not file_paths:
		print('\033[91m\033[1mNo dataset selected.\033[0m')
		return		
	print ('\033[92m\033[1mSelected Dataset:\033[0m')
	print(str(file_paths))	
	before = str(file_paths)
	output = str(output)

	def process_folder(before, output):
		for root, dirs, files in os.walk(before): 
			if 'anat' in dirs:
				anat_folder = os.path.join(root, 'anat')
				for file in os.listdir(anat_folder): 				          			       
					if file.endswith('T1w.nii.gz'):
						file_name = file.replace('.nii.gz', '')
						subfolder_path = os.path.join(output, file_name)
						os.makedirs(subfolder_path, exist_ok=True)
						file_path = os.path.join(anat_folder, file)
						os.system('cp '+file_path+' '+os.path.join(subfolder_path, file))
						
  				
	process_folder(before, output)                    						
	print('\n')
	print('\033[92m\033[1mRESULTS:\033[0m')
	print('\n')	
	def check_subfolders(directory, output_file_path):
		all_responses_are_one = True
		with open(output_file_path, 'w') as output_file:
			for subfolder in os.listdir(directory):
				subfolder_path = os.path.join(directory, subfolder)
				if os.path.isdir(subfolder_path):
					files = os.listdir(subfolder_path)
					if any('.nii.gz' in file for file in files):
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[92m\033[1mOK\033[0m")
						output_file.write(f"{subfolder}.nii.gz OK" + '\n')						
					elif not os.listdir(subfolder_path):
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}\033[0m \033[93m\033[1mEMPTY FOLDER\033[0m")
						output_file.write(f"{subfolder}.nii.gz EMPTY FOLDER" + '\n')						
					else:
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[91m\033[1mFAILED (MISSING SEGMENTATION FILE)\033[0m")
						output_file.write(f"{subfolder}.nii.gz FAILED (MISSING SEGMENTATION FILE)" + '\n')
                			
		if all_responses_are_one:
			print('\n')
			print("\033[92m\033[1mFOLDERS PREPARED!\033[0m")
		else:
			print('\n')
			print("\033[93m\033[1mFOLDERS PREPARED - CHECK THE WARNINGS\033[0m")
	
	if not os.listdir(before):
		print('\n')
		print("\033[91m\033[1mPREPARING FOLDERS FAILED\033[0m")
	else:	      			
		check_subfolders(str(output), str(output)+'/PrepareFoldersResults.txt')	   			
  
                          
#############################   

def modal_docker():
	
	print('\033[94m\033[1mPLEASE TYPE THE PATH OF THE\033[0m \033[92m\033[1mPREPARED\033[0m \033[94m\033[1mFOLDER:\033[0m')		 			 	       	
	file_paths = input("prepared folder path: ")
	if not file_paths:
		print('\033[91m\033[1mNo folder selected.\033[0m')
		return
		
	print ('\033[92m\033[1mSelected files:\033[0m')
	path = str(file_paths)
	dir_list = os.listdir(path)
	for i in dir_list:
		if '.txt' not in i:
			print(str(i)+'.nii.gz')
		
	before = str(file_paths)
           	            	 					
	exit_code = os.system("docker --version")
	if exit_code != 0:
    		print('\033[91m\033[1mDOCKER NOT INSTALLED. Please install Docker before running this script.\033[0m')
    		raise SystemExit(1)
    			
	password = None
	
	comando1='sudo -S docker stop vertebral_labeling'
	comando2='sudo -S docker rm vertebral_labeling'

	exit_code1 = subprocess.run('docker ps', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
	if exit_code1 != 0:
		if password == None:
			password = get_pass()	
		result = subprocess.check_output("sudo -S docker ps", shell=True, text=True, input=password)
		if 'vertebral_labeling' in result:
			subprocess.run(comando1, shell=True, check=True, input=password.encode())
			subprocess.run(comando2, shell=True, check=True, input=password.encode())
	else:
		result = subprocess.check_output("docker ps", shell=True, text=True)
		result = str(result)
		if 'vertebral_labeling' in result:
			os.system('docker stop vertebral_labeling')
			os.system('docker rm vertebral_labeling')
		
	exit_code2 = subprocess.run('docker ps -a', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
	if exit_code2 != 0:
		if password == None:
			password = get_pass()
		result = subprocess.check_output("sudo -S docker ps -a", shell=True, text=True, input=password)
		if 'vertebral_labeling' in result:
			subprocess.run(comando2, shell=True, check=True, input=password.encode())
	else:
		result = subprocess.check_output("docker ps", shell=True, text=True)
		result = str(result)
		if 'vertebral_labeling' in result:
			os.system('docker rm vertebral_labeling')
						
	loww1='docker run -itd --gpus all --ipc=host --name vertebral_labeling art2mri/vertebral_labeling:4.0'
	loww2='sudo -S docker run -itd --gpus all --ipc=host --name vertebral_labeling art2mri/vertebral_labeling:4.0'
	
	try:
		subprocess.run(loww1, shell=True, check=True, stderr=subprocess.DEVNULL)
	except subprocess.CalledProcessError as e:
			if password == None:
				password = get_pass()
			subprocess.run(loww2, shell=True, check=True, input=password.encode())		

	for i in (dir_list):
		if '.txt' not in i: 
			try:
				subprocess.run('docker start vertebral_labeling', shell=True, check=True, stderr=subprocess.DEVNULL)
			except subprocess.CalledProcessError as e:
				if password == None:
					password = get_pass()
				subprocess.run('sudo -S docker start vertebral_labeling', shell=True, check=True, input=password.encode())	

			command1 = 'cd '+before+'/'+str(i)+' && '+'docker cp '+before+'/'+str(i)+'/'+str(i)+'.nii.gz vertebral_labeling:/home/SCT/'+str(i)+'.nii.gz'+' && '+'docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling python3 spine.py'
			command2 = 'cd '+before+'/'+str(i)+' && '+'sudo docker cp '+before+'/'+str(i)+'/'+str(i)+'.nii.gz vertebral_labeling:/home/SCT/'+str(i)+'.nii.gz'+' && '+'sudo docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling python3 spine.py'
			get_exit(command1, command2)
											
			command3='docker exec -it vertebral_labeling chmod -R 777 /home/SCT/'+str(i)+'_seg.nii.gz'
			command4='sudo docker exec -it vertebral_labeling chmod -R 777 /home/SCT/'+str(i)+'_seg.nii.gz'
			get_exit(command3, command4)
						
			command5='docker exec -it vertebral_labeling chmod -R 777 /home/SCT/qc_'+str(i)
			command6='sudo docker exec -it vertebral_labeling chmod -R 777 /home/SCT/qc_'+str(i)
			exit3 = subprocess.run(command5, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
			get_exit(command5, command6)
		
			command7='docker cp vertebral_labeling:/home/SCT/'+str(i)+'_seg.nii.gz'+' '+before+'/'+str(i)+'/'+str(i)+'_seg.nii.gz'
			command8='sudo docker cp vertebral_labeling:/home/SCT/'+str(i)+'_seg.nii.gz'+' '+before+'/'+str(i)+'/'+str(i)+'_seg.nii.gz'
			get_exit(command7, command8)
		
			command9='docker cp vertebral_labeling:/home/SCT/qc_'+str(i)+' '+before+'/'+str(i)+'/qc_'+str(i)
			command10='sudo docker cp vertebral_labeling:/home/SCT/qc_'+str(i)+' '+before+'/'+str(i)+'/qc_'+str(i)
			exit5 = subprocess.run(command9, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
			get_exit(command9, command10)
		
			command11='docker exec -it vertebral_labeling rm -f /home/SCT/'+str(i)+'_seg.nii.gz'
			command12='sudo docker exec -it vertebral_labeling rm -f /home/SCT/'+str(i)+'_seg.nii.gz'
			get_exit(command11, command12)
		
			command13='docker exec -it vertebral_labeling rm -f /home/SCT/'+str(i)+'.nii.gz'
			command14='sudo docker exec -it vertebral_labeling rm -f /home/SCT/'+str(i)+'.nii.gz'
			get_exit(command13, command14)
		
			command15='docker exec -it vertebral_labeling rm -r /home/SCT/qc_'+str(i)
			command16='sudo docker exec -it vertebral_labeling rm -r /home/SCT/qc_'+str(i)
			get_exit(command15, command16)
					
	command17='docker stop vertebral_labeling'
	command18='sudo -S docker stop vertebral_labeling'
	exit9 = subprocess.run(command17, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
	if exit9 != 0:
		if password == None:
			password = get_pass()
		subprocess.run(command18, shell=True, check=True, input=password.encode())
	else:
		os.system(command17)
	command19='docker rm vertebral_labeling'
	command20='sudo -S docker rm vertebral_labeling'
	exit10 = subprocess.run(command19, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
	if exit10 != 0:
		if password == None:
			password = get_pass()
		subprocess.run(command20, shell=True, check=True, input=password.encode())
	else:
		os.system(command19)
				
	print('\n')
	print('\033[92m\033[1mRESULTS:\033[0m')
	print('\n')	
	
	def check_subfolders(directory, output_file_path):
		all_responses_are_one = True
		with open(output_file_path, 'w') as output_file:
			for subfolder in os.listdir(directory):
				subfolder_path = os.path.join(directory, subfolder)
				if os.path.isdir(subfolder_path):
					files = os.listdir(subfolder_path)
					if any('_seg.nii.gz' in file for file in files):
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[92m\033[1mOK\033[0m")
						output_file.write(f"{subfolder}.nii.gz OK" + '\n')						
					elif not os.listdir(subfolder_path):
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}\033[0m \033[93m\033[1mEMPTY FOLDER\033[0m")
						output_file.write(f"{subfolder} EMPTY FOLDER" + '\n')						
					else:
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[91m\033[1mFAILED (MISSING SEGMENTATION FILE)\033[0m")
						output_file.write(f"{subfolder}.nii.gz FAILED (MISSING SEGMENTATION FILE)" + '\n')
                			
		if all_responses_are_one:
			print('\n')
			print("\033[92m\033[1mSEGMENTATION FINISHED\033[0m")
		else:
			print('\n')
			print("\033[93m\033[1mSEGMENTATION FINISHED WITH WARNINGS\033[0m")
	
	if not os.listdir(before):
		print('\n')
		print("\033[91m\033[1mSEGMENTATION FAILED\033[0m")
	else:	      			
		check_subfolders(str(before), str(before)+'/SegmentationResults.txt')		
	
#############################

def modal_singularity():			 			 	       	
	print('\033[94m\033[1mPLEASE TYPE THE PATH OF THE\033[0m \033[92m\033[1mEnigma-SC\033[0m \033[94m\033[1mFOLDER\033[0m')
	enigma_folder = input("Enigma-SC folder path: ")
	if not enigma_folder:
		print('\033[91m\033[1mNo folder selected.\033[0m')
		return
	print('The \033[92m\033[1mEnigma-SC\033[0m folder selected is located at: '+enigma_folder)
	
	print('\033[94m\033[1mNOW TYPE THE PATH OF THE\033[0m \033[92m\033[1mPREPARED\033[0m \033[94m\033[1mFOLDER:\033[0m')		 			 	       	
	file_paths = input("Prepared folder path: ")
	if not file_paths:
		print('\033[91m\033[1mNo folders selected.\033[0m')
		return
		
	print ('\033[92m\033[1mSelected files:\033[0m')
	path = str(file_paths)
	dir_list2 = os.listdir(path)
	for i in dir_list2:
		if '.txt' not in i:
			print(str(i)+'.nii.gz')
		
	before = str(file_paths)          	            	 			
		
	exit_code = os.system("singularity --version")
	exity_code = os.system("apptainer --version")
	if exit_code and exity_code != 0:
    		print('\033[91m\033[1mSINGULARITY AND APPTAINER NOT INSTALLED. Please install one of them before running this script.\033[0m')
    		raise SystemExit(1)		
		
	k = os.listdir(enigma_folder+'/vertebral_labeling.simg/home/SCT/')
	for i in k:
		if os.path.isdir(enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)):
			shutil.rmtree(enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i))
		else:
			os.remove(enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i))		
	path = enigma_folder+'/vertebral_labeling.simg/home'
	dir_list = os.listdir(path)		
	for i in dir_list:
		if 'SCT' not in i:
			if 'datav2' not in i:
				if 'scripts' not in i:
					command21='rm -rf '+path+'/'+str(i)
					command22='sudo rm -rf '+path+'/'+str(i)
					get_exit(command21, command22)		
    	 
	for i in dir_list2: 
		if '.txt' not in i:
			if any(arq.endswith('.nii.gz') for arq in os.listdir('vertebral_labeling.simg/home/SCT/')):
				command23='rm vertebral_labeling.simg/home/SCT/*nii.gz'
				command24='sudo rm vertebral_labeling.simg/home/SCT/*nii.gz'
				get_exit(command23, command24)
			if any(arq.endswith('.cache') for arq in os.listdir('vertebral_labeling.simg/home/SCT/')):
				command25='rm vertebral_labeling.simg/home/SCT/*nii.gz'
				command26='sudo rm vertebral_labeling.simg/home/SCT/*nii.gz'
				get_exit(command25, command26)			
			os.system ('cd '+before+'/'+str(i))
			command27='cd '+before+'/'+str(i)+' && '+'cp '+before+'/'+str(i)+'/'+str(i)+'.nii.gz '+enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)+'.nii.gz'
			command28='cd '+before+'/'+str(i)+' && '+'sudo cp '+before+'/'+str(i)+'/'+str(i)+'.nii.gz '+enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)+'.nii.gz'
			get_exit(command27, command28)
			command29='chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)+'.nii.gz'
			command30='sudo chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)+'.nii.gz'
			get_exit(command29, command30)				
			try:
				command31='singularity exec --writable vertebral_labeling.simg/ python3 /spine.py'
				command32='sudo singularity exec --writable vertebral_labeling.simg/ python3 /spine.py'
				get_exit(command31, command32)		
			except subprocess.CalledProcessError:
				command33='apptainer exec --writable vertebral_labeling.simg/ python3 /spine.py'
				command34='sudo apptainer exec --writable vertebral_labeling.simg/ python3 /spine.py'
				get_exit(command33, command34)
			command35='chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)+'_seg.nii.gz'
			command36='sudo chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)+'_seg.nii.gz'
			get_exit(command35, command36)				
			try:
				command37='singularity exec --writable vertebral_labeling.simg/ chmod -R 777 /home/SCT/qc_'+str(i)
				command38='sudo singularity exec --writable vertebral_labeling.simg/ chmod -R 777 /home/SCT/qc_'+str(i)
				get_exit(command37, command38)
			except subprocess.CalledProcessError:
				command39='apptainer exec --writable vertebral_labeling.simg/ chmod -R 777 /home/SCT/qc_'+str(i)
				command40='sudo apptainer exec --writable vertebral_labeling.simg/ chmod -R 777 /home/SCT/qc_'+str(i)
				get_exit(command39, command40)	
			command41='mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/'+str(i)+'_seg.nii.gz '+before+'/'+str(i)
			subprocess.run(command41, shell=True, check=True)
			command47='mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/qc_'+str(i)+' '+before+'/'+str(i)+'/qc_'+str(i)
			subprocess.run(command47, shell=True, check=True)
			try:
				command49='singularity exec --writable --nv vertebral_labeling.simg/ rm -f /home/SCT/'+str(i)+'.nii.gz'
				command50='sudo singularity exec --writable --nv vertebral_labeling.simg/ rm -f /home/SCT/'+str(i)+'.nii.gz'
				get_exit(command49, command50)
			except subprocess.CalledProcessError:
				command51='apptainer exec --writable --nv vertebral_labeling.simg/ rm -f /home/SCT/'+str(i)+'.nii.gz'
				command52='sudo apptainer exec --writable --nv vertebral_labeling.simg/ rm -f /home/SCT/'+str(i)+'.nii.gz'	
				get_exit(command51, command52)	

	print('\n')
	print('\033[92m\033[1mRESULTS:\033[0m')
	print('\n')	
	def check_subfolders(directory, output_file_path):
		all_responses_are_one = True
		with open(output_file_path, 'w') as output_file:
			for subfolder in os.listdir(directory):
				subfolder_path = os.path.join(directory, subfolder)
				if os.path.isdir(subfolder_path):
					files = os.listdir(subfolder_path)
					if any('_seg.nii.gz' in file for file in files):
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[92m\033[1mOK\033[0m")
						output_file.write(f"{subfolder}.nii.gz OK" + '\n')						
					elif not os.listdir(subfolder_path):
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}\033[0m \033[93m\033[1mEMPTY FOLDER\033[0m")
						output_file.write(f"{subfolder} EMPTY FOLDER" + '\n')						
					else:
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[91m\033[1mFAILED (MISSING SEGMENTATION FILE)\033[0m")
						output_file.write(f"{subfolder}.nii.gz FAILED (MISSING SEGMENTATION FILE)" + '\n')
                			
		if all_responses_are_one:
			print('\n')
			print("\033[92m\033[1mSEGMENTATION FINISHED\033[0m")
		else:
			print('\n')
			print("\033[93m\033[1mSEGMENTATION FINISHED WITH WARNINGS\033[0m")
	
	if not os.listdir(before):
		print('\n')
		print("\033[91m\033[1mSEGMENTATION FAILED\033[0m")
	else:	      			
		check_subfolders(str(before), str(before)+'/SegmentationResults.txt')	   

#############################  

def docker():

	print('\033[94m\033[1mPLEASE TYPE THE PATH OF THE\033[0m \033[92m\033[1mPREPARED\033[0m \033[94m\033[1mFOLDER:\033[0m')
	file_paths = input("Prepared folder path: ")
	if not file_paths:
		print('\033[91m\033[1mNo folders selected.\033[0m')
		return
		
	print ('\033[92m\033[1mSelected files:\033[0m')
	path = str(file_paths)
	dir_list = os.listdir(path)
	for i in dir_list:
		if '.txt' not in i:
			print(str(i)+'.nii.gz')
		
	before = str(file_paths)			
		
	exit_code = os.system("docker --version")
	if exit_code != 0:
    		print('\033[91m\033[1mDOCKER NOT INSTALLED. Please install Docker before running this script.\033[0m')
    		raise SystemExit(1)
    		
	password = None		
		
	comando1='sudo -S docker stop vertebral_labeling'
	comando2='sudo -S docker rm vertebral_labeling'

	exit_code1 = subprocess.run('docker ps', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
	if exit_code1 != 0:
		if password == None:
			password = get_pass()	
		result = subprocess.check_output("sudo -S docker ps", shell=True, text=True, input=password)
		if 'vertebral_labeling' in result:
			subprocess.run(comando1, shell=True, check=True, input=password.encode('utf-8'))
			subprocess.run(comando2, shell=True, check=True, input=password.encode('utf-8'))
	else:
		result = subprocess.check_output("docker ps", shell=True, text=True)
		result = str(result)
		if 'vertebral_labeling' in result:
			os.system('docker stop vertebral_labeling')
			os.system('docker rm vertebral_labeling')
		
	exit_code2 = subprocess.run('docker ps -a', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
	if exit_code2 != 0:
		if password == None:
			password = get_pass()
		result = subprocess.check_output("sudo -S docker ps -a", shell=True, text=True, input=password)
		if 'vertebral_labeling' in result:
			subprocess.run(comando2, shell=True, check=True, input=password.encode('utf-8'))
	else:
		result = subprocess.check_output("docker ps", shell=True, text=True)
		result = str(result)
		if 'vertebral_labeling' in result:
			os.system('docker rm vertebral_labeling')																	
	try:
    		subprocess.run('nvidia-smi', check=True)
    		docker_command = 'docker run -itd --gpus all --ipc=host --name vertebral_labeling art2mri/vertebral_labeling:4.0'
	except FileNotFoundError as gpu_error:
    		print(f"Error checking for GPU: {gpu_error}")
    		docker_command = 'docker run -itd --ipc=host --name vertebral_labeling art2mri/vertebral_labeling:4.0'
	except subprocess.CalledProcessError as gpu_error:
    		print(f"Error checking for GPU: {gpu_error}")
    		docker_command = 'docker run -itd --ipc=host --name vertebral_labeling art2mri/vertebral_labeling:4.0'	
	try:
    		subprocess.run(docker_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
	except subprocess.CalledProcessError as docker_error:
		if password == None:
			password = get_pass()
		subprocess.run('sudo -S '+docker_command2, shell=True, check=True, input=password.encode('utf-8'))	
		print(f"Error running Docker command: {docker_error}")
    		   		    			
	loww1='docker run -itd --gpus all --ipc=host --name vertebral_labeling art2mri/vertebral_labeling:4.0'
	loww2='sudo -S docker run -itd --gpus all --ipc=host --name vertebral_labeling art2mri/vertebral_labeling:4.0'
	try:
		subprocess.run(loww1, shell=True, check=True, stderr=subprocess.DEVNULL)
	except subprocess.CalledProcessError as e:
			if password == None:
				password = get_pass()
			subprocess.run(loww2, shell=True, check=True, input=password.encode('utf-8'))
							
	for i in (dir_list):
		if '.txt' not in i:
			command53='docker cp '+before+'/'+str(i)+'/'+str(i)+'.nii.gz vertebral_labeling:/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/'+str(i)+'_0000.nii.gz'
			command54='sudo -S docker cp '+before+'/'+str(i)+'/'+str(i)+'.nii.gz vertebral_labeling:/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/'+str(i)+'_0000.nii.gz'
			try:
				subprocess.run(command53, shell=True, check=True, stderr=subprocess.DEVNULL)
			except subprocess.CalledProcessError as e:
				if password == None:
					password = get_pass()
				subprocess.run(command54, shell=True, check=True, input=password.encode('utf-8'))
			command55='docker start vertebral_labeling'
			command56='sudo -S docker start vertebral_labeling'
			try:
				subprocess.run(command55, shell=True, check=True, stderr=subprocess.DEVNULL)
			except subprocess.CalledProcessError as e:
				if password == None:
					password = get_pass()
				subprocess.run(command56, shell=True, check=True, input=password.encode('utf-8'))					
			comando_11 = 'docker exec -it vertebral_labeling python3 /home/scripts/cuda.py'
			comando_12 = 'sudo -S docker exec -it vertebral_labeling python3 /home/scripts/cuda.py'
			comando_2 = 'sudo docker exec -it vertebral_labeling python3 /home/scripts/cpu.py'
			command_1 = 'sudo docker exec -it vertebral_labeling python3 /home/scripts/cuda.py'
			file_to_check = '/home/datav2/inference/761_SCT/preds/'+str(i)+'.nii.gz'
			command_21 = 'docker exec -it vertebral_labeling python3 /home/scripts/cpu.py'
			command_22 = 'sudo -S docker exec -it vertebral_labeling python3 /home/scripts/cpu.py'
			exit16 = subprocess.run(comando_11, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
			if exit16 != 0:
				os.system('sudo docker exec -it vertebral_labeling python3 /home/scripts/cuda.py')
			else:
				os.system('docker exec -it vertebral_labeling python3 /home/scripts/cuda.py')	
				
			check_file_command1 = f'docker exec -it vertebral_labeling test -f {file_to_check} && echo "found" || echo "not found"'	      				
			check_file_command2 = f'sudo -S docker exec -it vertebral_labeling test -f {file_to_check} && echo "found" || echo "not found"'
			exit15 = subprocess.run(check_file_command1, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
			if exit15 != 0:
				check_file_command = check_file_command2
			else:
				check_file_command = check_file_command1
			
			check_result = subprocess.run(check_file_command, shell=True, stdout=subprocess.PIPE, text=True)
			if "not found" in check_result.stdout:
				print("\033[93mTried to predict on GPU, but your GPU is not able to work on this task. Please check your CUDA settings\033[0m")
				print('\033[95m\033[1mNow trying to perform on CPU, this may take much more time to finish\033[0m')
				exit16 = subprocess.run(command_21, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
				if exit16 != 0:
					os.system('sudo docker exec -it vertebral_labeling python3 /home/scripts/cpu.py')
				else:
					os.system('docker exec -it vertebral_labeling python3 /home/scripts/cpu.py')
			command555='docker exec -it vertebral_labeling chmod -R 777 /home/datav2/inference/761_SCT/preds/'+str(i)+'.nii.gz'
			command666='sudo docker exec -it vertebral_labeling chmod -R 777 /home/datav2/inference/761_SCT/preds/'+str(i)+'.nii.gz'
			get_exit(command555, command666)
			command515='docker cp vertebral_labeling:/home/datav2/inference/761_SCT/preds/'+str(i)+'.nii.gz'+' '+before+'/'+str(i)+'/'+str(i)+'_seg_labeled.nii.gz'
			command616='sudo docker cp vertebral_labeling:/home/datav2/inference/761_SCT/preds/'+str(i)+'.nii.gz'+' '+before+'/'+str(i)+'/'+str(i)+'_seg_labeled.nii.gz'
			get_exit(command515, command616)
			command575='docker exec -it vertebral_labeling rm -f /home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/'+str(i)+'_0000.nii.gz'
			command676='sudo docker exec -it vertebral_labeling rm -f /home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/'+str(i)+'_0000.nii.gz'
			get_exit(command575, command676)		
			os.system('cd '+before+'/'+str(i)+' && sct_qc -i '+str(i)+'.nii.gz -s '+str(i)+'_seg_labeled.nii.gz'+' -p sct_label_vertebrae')
			os.system('mv -v '+before+'/'+str(i)+'/qc '+before+'/'+str(i)+'/qc_labeled_'+str(i))	
	command63='docker stop vertebral_labeling'
	command64='sudo -S docker stop vertebral_labeling'
	exit19 = subprocess.run(command63, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
	if exit19 != 0:
		if password == None:
			password = get_pass()
		subprocess.run(command64, shell=True, check=True, input=password.encode('utf-8'))
	else:
		os.system(command63)
	command65='docker rm vertebral_labeling'
	command66='sudo -S docker rm vertebral_labeling'
	exit20 = subprocess.run(command65, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
	if exit20 != 0:
		if password == None:
			password = get_pass()
		subprocess.run(command66, shell=True, check=True, input=password.encode('utf-8'))
	else:
		os.system(command65)
	print('\n')
	print('\033[92m\033[1mRESULTS:\033[0m')
	print('\n')
	def check_subfolders(directory, output_file_path):
		all_responses_are_one = True
		with open(output_file_path, 'w') as output_file:
			for subfolder in os.listdir(directory):
				subfolder_path = os.path.join(directory, subfolder)
				if os.path.isdir(subfolder_path):
					files = os.listdir(subfolder_path)
					if any('_seg_labeled.nii.gz' in file for file in files):
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[92m\033[1mOK\033[0m")
						output_file.write(f"{subfolder}.nii.gz OK" + '\n')						
					elif not os.listdir(subfolder_path):
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}\033[0m \033[93m\033[1mEMPTY FOLDER\033[0m")
						output_file.write(f"{subfolder} EMPTY FOLDER" + '\n')						
					else:
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[91m\033[1mFAILED (MISSING LABELED FILE)\033[0m")
						output_file.write(f"{subfolder}.nii.gz FAILED (MISSING LABELED FILE)" + '\n')
                			
		if all_responses_are_one:
			print('\n')
			print("\033[92m\033[1mAUTOMATED LABELING FINISHED\033[0m")
		else:
			print('\n')
			print("\033[93m\033[1mAUTOMATED LABELING FINISHED WITH WARNINGS\033[0m")
	
	if not os.listdir(before):
		print('\n')
		print("\033[91m\033[1mSEGMENTATION FAILED\033[0m")
	else:	      			
		check_subfolders(str(before), str(before)+'/AutomatedLabelingResults.txt')
	#pass
	
#############################		

def singularity():
	print('\033[94m\033[1mPLEASE TYPE THE PATH OF THE\033[0m \033[92m\033[1mEnigma-SC\033[0m \033[94m\033[1mFOLDER\033[0m')
	enigma_folder = input("Enigma-SC folder path: ")
	print('The \033[92m\033[1mEnigma-SC\033[0m folder selected is located at: '+enigma_folder)
	
	print('\033[94m\033[1mPLEASE TYPE THE PATH OF THE\033[0m \033[92m\033[1mPREPARED\033[0m \033[94m\033[1mFOLDER:\033[0m')
	file_paths = input("Prepared folder path: ")
	if not file_paths:
		print('\033[91m\033[1mNo folders selected.\033[0m')
		return
		
	print ('\033[92m\033[1mSelected files:\033[0m')
	path = str(file_paths)
	dir_list2 = os.listdir(path)
	for i in dir_list2:
		if '.txt' not in i:
			print(str(i)+'.nii.gz')
		
	before = str(file_paths)

	exit_code = os.system("singularity --version")
	exity_code = os.system("apptainer --version")
	if exit_code and exity_code != 0:
    		print('\033[91m\033[1mSINGULARITY AND APPTAINER NOT INSTALLED. Please install one of them before running this script.\033[0m')
    		raise SystemExit(1)		
	password = None
	
	k = os.listdir(enigma_folder+'/vertebral_labeling.simg/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/')
	for i in k:
		if os.path.isdir(enigma_folder+'/vertebral_labeling.simg/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/'+str(i)):
			shutil.rmtree(enigma_folder+'/vertebral_labeling.simg/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/'+str(i))
		else:
			os.remove(enigma_folder+'/vertebral_labeling.simg/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/'+str(i))	
	path = enigma_folder+'/vertebral_labeling.simg/home'
	dir_list = os.listdir(path)		
	for i in dir_list:
		if 'SCT' not in i:
			if 'datav2' not in i:
				if 'scripts' not in i:
					command21='rm -rf '+path+'/'+str(i)
					command22='sudo -S rm -rf '+path+'/'+str(i)
					exit2 = subprocess.run(command21, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
					if exit2 != 0:
						if password == None:
							password = get_pass()
						subprocess.run(command22, shell=True, check=True, input=password.encode('utf-8'))
					else:
						os.system(command21)
					
	for i in dir_list2:
		if '.txt' not in i:
			if any(arq.endswith('.nii.gz') for arq in os.listdir('vertebral_labeling.simg/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/')):
				command219='rm vertebral_labeling.simg/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/*nii.gz'
				command222='sudo -S rm vertebral_labeling.simg/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/*nii.gz'
				exit238 = subprocess.run(command219, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
				if exit238 != 0:
					if password == None:
						password = get_pass()
					subprocess.run(command222, shell=True, check=True, input=password.encode('utf-8'))
				else:
					os.system(command219)	
			command67='cp '+before+'/'+str(i)+'/'+str(i)+'.nii.gz '+enigma_folder
			command68='sudo cp '+before+'/'+str(i)+'/'+str(i)+'.nii.gz '+enigma_folder
			get_exit(command67, command68)
			command69='chmod -R 777 '+enigma_folder+'/'+str(i)+'.nii.gz'
			command70='sudo chmod -R 777 '+enigma_folder+'/'+str(i)+'.nii.gz'
			get_exit(command69, command70)
			try:
				os.system('mv '+str(i)+'.nii.gz '+'vertebral_labeling.simg/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/'+str(i)+'_0000.nii.gz')
			except subprocess.CalledProcessError as e:
				os.system('sudo mv '+str(i)+'.nii.gz '+'vertebral_labeling.simg/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/'+str(i)+'_0000.nii.gz')	
			command73='chmod -R 777 vertebral_labeling.simg/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/'+str(i)+'_0000.nii.gz'
			command74='sudo chmod -R 777 vertebral_labeling.simg/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/'+str(i)+'_0000.nii.gz'
			get_exit(command73, command74)
			try:
				subprocess.run(["singularity --version"], check=True, shell=True)
				command_1 = 'singularity exec --writable --nv vertebral_labeling.simg/ python3 /home/scripts/cuda.py'
				command_12 = 'sudo singularity exec --writable --nv vertebral_labeling.simg/ python3 /home/scripts/cuda.py'
				command_2 = 'singularity exec --writable --nv vertebral_labeling.simg/ python3 /home/scripts/cpu.py'
				command_22= 'sudo singularity exec --writable --nv vertebral_labeling.simg/ python3 /home/scripts/cpu.py'
				exit333 = subprocess.run(command_1, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
				if exit333 != 0:
					command111 = command_12
				else:
					command111 = command_1
				try:
        				subprocess.check_call(command111, shell=True, stderr=subprocess.DEVNULL)	
				except subprocess.CalledProcessError as e:
					pass  
				dire = 'vertebral_labeling.simg/home/datav2/inference/761_SCT/preds/'
				file1 = str(i)+'.nii.gz'
				way = os.path.join(dire, file1)	     				
				if os.path.exists(way):
					print('OK')
				else:	
					print("\033[93mTried to predict on GPU, but your GPU is not able to work on this task. Please check your CUDA settings\033[0m")
					print('\033[95m\033[1mNow trying to perform on CPU, this may take much more time to finish\033[0m')
					exit339 = subprocess.run(command_2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
					if exit339 != 0:
						command211 = command_22
					else:
						command211 = command_2
					subprocess.run(command211, shell=True)
			except subprocess.CalledProcessError:
				command_11 = 'apptainer exec --writable --nv vertebral_labeling.simg/ python3 /home/scripts/cuda.py'
				command_11_1 = 'sudo apptainer exec --writable --nv vertebral_labeling.simg/ python3 /home/scripts/cuda.py'
				command_22 = 'apptainer exec --writable --nv vertebral_labeling.simg/ python3 /home/scripts/cpu.py'
				command_22_2 = 'sudo apptainer exec --writable --nv vertebral_labeling.simg/ python3 /home/scripts/cpu.py'
				exit3333 = subprocess.run(command_11, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
				if exit3333 != 0:
					command1111 = command_11_1
				else:
					command1111 = command_11
				try:
        				subprocess.check_call(command1111, shell=True, stderr=subprocess.DEVNULL)	
				except subprocess.CalledProcessError as e:
					pass  
				dire = 'vertebral_labeling.simg/home/datav2/inference/761_SCT/preds/'
				file1 = str(i)+'.nii.gz'
				way = os.path.join(dire, file1)	     				
				if os.path.exists(way):
					print('OK')
				else:	
					print("\033[93mTried to predict on GPU, but your GPU is not able to work on this task. Please check your CUDA settings\033[0m")
					print('\033[95m\033[1mNow trying to perform on CPU, this may take much more time to finish\033[0m')
					exit338 = subprocess.run(command_22, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
					if exit338 != 0:
						command221 = command_22_2
					else:
						ommand221 = command_22
					subprocess.run(command_221, shell=True)
			command75='chmod -R 777 vertebral_labeling.simg/home/datav2/inference/761_SCT/preds/'+str(i)+'.nii.gz'
			command76='sudo chmod -R 777 vertebral_labeling.simg/home/datav2/inference/761_SCT/preds/'+str(i)+'.nii.gz'			
			get_exit(command75, command76)
			os.system('mv -v '+enigma_folder+'/vertebral_labeling.simg/home/datav2/inference/761_SCT/preds/'+str(i)+'.nii.gz '+enigma_folder+'/vertebral_labeling.simg/home/datav2/inference/761_SCT/preds/'+str(i)+'_seg_labeled.nii.gz')
			try:
				os.system('rm vertebral_labeling.simg/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/*nii.gz')
			except subprocess.CalledProcessError as e:
				os.system('sudo rm vertebral_labeling.simg/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/*nii.gz')
			try:
				os.system('mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/datav2/inference/761_SCT/preds/'+str(i)+'_seg_labeled.nii.gz '+enigma_folder)
			except subprocess.CalledProcessError as e:
				os.system('sudo mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/datav2/inference/761_SCT/preds/'+str(i)+'_seg_labeled.nii.gz '+enigma_folder)			
			try:
				os.system('mv '+enigma_folder+'/'+str(i)+'_seg_labeled.nii.gz '+before+'/'+str(i))
			except subprocess.CalledProcessError as e:
				os.system('sudo mv '+enigma_folder+'/'+str(i)+'_seg_labeled.nii.gz '+before+'/'+str(i))
			os.system('cd '+before+'/'+str(i)+' && sct_qc -i '+str(i)+'.nii.gz -s '+str(i)+'_seg_labeled.nii.gz'+' -p sct_label_vertebrae')
			try:
				os.system('mv -v '+before+'/'+str(i)+'/qc '+before+'/'+str(i)+'/qc_labeled_'+str(i))
			except subprocess.CalledProcessError as e:
				os.system('sudo mv -v '+before+'/'+str(i)+'/qc '+before+'/'+str(i)+'/qc_labeled_'+str(i))
	print('\n')
	print('\033[92m\033[1mRESULTS:\033[0m')
	print('\n')
	def check_subfolders(directory, output_file_path):
		all_responses_are_one = True
		with open(output_file_path, 'w') as output_file:
			for subfolder in os.listdir(directory):
				subfolder_path = os.path.join(directory, subfolder)
				if os.path.isdir(subfolder_path):
					files = os.listdir(subfolder_path)
					if any('_seg_labeled.nii.gz' in file for file in files):
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[92m\033[1mOK\033[0m")
						output_file.write(f"{subfolder}.nii.gz OK" + '\n')						
					elif not os.listdir(subfolder_path):
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}\033[0m \033[93m\033[1mEMPTY FOLDER\033[0m")
						output_file.write(f"{subfolder} EMPTY FOLDER" + '\n')						
					else:
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[91m\033[1mFAILED (MISSING LABELED FILE)\033[0m")
						output_file.write(f"{subfolder}.nii.gz FAILED (MISSING LABELED FILE)" + '\n')
                			
		if all_responses_are_one:
			print('\n')
			print("\033[92m\033[1mAUTOMATED LABELING FINISHED\033[0m")
		else:
			print('\n')
			print("\033[93m\033[1mAUTOMATED LABELING FINISHED WITH WARNINGS\033[0m")
	
	if not os.listdir(before):
		print('\n')
		print("\033[91m\033[1mSEGMENTATION FAILED\033[0m")
	else:	      			
		check_subfolders(str(before), str(before)+'/AutomatedLabelingResults.txt')
		
															
#############################  

def manual():	 
	
	print('\033[94m\033[1mPLEASE TYPE THE PATH OF THE PREPARED FOLDER.\033[0m \033[92m\033[1mCREATE A FOLDER CONTAINING ONLY THE FOLDERS WHICH\033[0m \033[94m\033[1m AUTOMATED VERTEBRAL LABELING STEP HAVE PREVIOUSLY FAILED:\033[0m')
	file_paths = input("PATH OF THE FOLDER CONTAINING THE FOLDERS WHICH FAILED ON AUTOMATED VERTEBRAL LABELING STEP: ")
	if not file_paths:
		print('\033[91m\033[1mNo folders selected.\033[0m')
		return
		
	print ('\033[92m\033[1mSelected files:\033[0m')
	path = str(file_paths)
	dir_list = os.listdir(path)
	for i in dir_list:
		if '.txt' not in i:
			print(str(i)+'.nii.gz')
		
	before = str(file_paths)	
		
	for i in dir_list:
		if '.txt' not in i:
			os.system('cd '+before+'/'+str(i)+' && sct_label_utils -i '+str(i)+'.nii.gz'+' -create-viewer 2,3 -o '+str(i)+'_labels_disc.nii.gz')
	print('\n')
	print('\033[92m\033[1mRESULTS:\033[0m')
	print('\n')
	def check_subfolders(directory, output_file_path):
		all_responses_are_one = True
		with open(output_file_path, 'w') as output_file:
			for subfolder in os.listdir(directory):
				subfolder_path = os.path.join(directory, subfolder)
				if os.path.isdir(subfolder_path):
					files = os.listdir(subfolder_path)
					if any('_labels_disc.nii.gz' in file for file in files):
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[92m\033[1mOK\033[0m")
						output_file.write(f"{subfolder}.nii.gz OK" + '\n')						
					elif not os.listdir(subfolder_path):
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}\033[0m \033[93m\033[1mEMPTY FOLDER\033[0m")
						output_file.write(f"{subfolder} EMPTY FOLDER" + '\n')						
					else:
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[93m\033[1mNOT SELECTED\033[0m")
						output_file.write(f"{subfolder}.nii.gz NOT SELECTED" + '\n')
	
		if all_responses_are_one:
			print('\n')
			print("\033[92m\033[1mMANUAL LABELING FINISHED\033[0m")
		else:
			print('\n')
			print("\033[93m\033[1mMANUAL LABELING FINISHED WITH WARNINGS\033[0m")
	
	if not os.listdir(before):
		print('\n')
		print("\033[91m\033[1mMANUAL LABELING FAILED\033[0m")
	else:	      			
		check_subfolders(str(before), str(before)+'/ManualLabelingResults.txt')	

#############################

def reg_aut_docker():
	
	print('\033[94m\033[1mPLEASE TYPE THE PATH OF THE\033[0m \033[92m\033[1mPREPARED\033[0m \033[94m\033[1mFOLDER:\033[0m')
	file_paths = input("Prepared folder path: ")
	if not file_paths:
		print('\033[91m\033[1mNo folders selected.\033[0m')
		return
		
	print ('\033[92m\033[1mSelected files:\033[0m')
	path = str(file_paths)
	dir_list = os.listdir(path)
	for i in dir_list:
		if '.txt' not in i:
			print(str(i)+'.nii.gz')
		
	before = str(file_paths)	
		
	exit_code = os.system("docker --version")
	if exit_code != 0:
    		print('\033[91m\033[1mDOCKER NOT INSTALLED. Please install Docker before running this script.\033[0m')
    		raise SystemExit(1)
    		
	password = None	
    				
	comando1='sudo -S docker stop vertebral_labeling'
	comando2='sudo -S docker rm vertebral_labeling'

	exit_code1 = subprocess.run('docker ps', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
	if exit_code1 != 0:
		if password == None:
			password = get_pass()	
		result = subprocess.check_output("sudo -S docker ps", shell=True, text=True, input=password)
		if 'vertebral_labeling' in result:
			subprocess.run(comando1, shell=True, check=True, input=password.encode('utf-8'))
			subprocess.run(comando2, shell=True, check=True, input=password.encode('utf-8'))
	else:
		result = subprocess.check_output("docker ps", shell=True, text=True)
		result = str(result)
		if 'vertebral_labeling' in result:
			os.system('docker stop vertebral_labeling')
			os.system('docker rm vertebral_labeling')
		
	exit_code2 = subprocess.run('docker ps -a', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
	if exit_code2 != 0:
		if password == None:
			password = get_pass()
		result = subprocess.check_output("sudo -S docker ps -a", shell=True, text=True, input=password)
		if 'vertebral_labeling' in result:
			subprocess.run(comando2, shell=True, check=True, input=password.encode('utf-8'))
	else:
		result = subprocess.check_output("docker ps", shell=True, text=True)
		result = str(result)
		if 'vertebral_labeling' in result:
			os.system('docker rm vertebral_labeling')																	
	try:
    		subprocess.run('nvidia-smi', check=True)
    		docker_command = 'docker run -itd --gpus all --ipc=host --name vertebral_labeling art2mri/vertebral_labeling:4.0'
	except FileNotFoundError as gpu_error:
    		print(f"Error checking for GPU: {gpu_error}")
    		docker_command = 'docker run -itd --ipc=host --name vertebral_labeling art2mri/vertebral_labeling:4.0'
	except subprocess.CalledProcessError as gpu_error:
    		print(f"Error checking for GPU: {gpu_error}")
    		docker_command = 'docker run -itd --ipc=host --name vertebral_labeling art2mri/vertebral_labeling:4.0'	
	try:
    		subprocess.run(docker_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
	except subprocess.CalledProcessError as docker_error:
		if password == None:
			password = get_pass()
		subprocess.run('sudo -S '+docker_command2, shell=True, check=True, input=password.encode('utf-8'))	
		print(f"Error running Docker command: {docker_error}")
    		   		    			
	loww1='docker run -itd --gpus all --ipc=host --name vertebral_labeling art2mri/vertebral_labeling:4.0'
	loww2='sudo -S docker run -itd --gpus all --ipc=host --name vertebral_labeling art2mri/vertebral_labeling:4.0'
	
	try:
		subprocess.run(loww1, shell=True, check=True, stderr=subprocess.DEVNULL)
	except subprocess.CalledProcessError as e:
			if password == None:
				password = get_pass()
			subprocess.run(loww2, shell=True, check=True, input=password.encode('utf-8'))				
		
	for i in dir_list:
		if '.txt' not in i:
			try:
				subprocess.run('docker start vertebral_labeling', shell=True, check=True, stderr=subprocess.DEVNULL)
			except subprocess.CalledProcessError as e:
				if password == None:
					password = get_pass()
				subprocess.run('sudo -S docker start vertebral_labeling', shell=True, check=True, input=password.encode())
			command77='cd '+before+'/'+str(i)+' && '+'docker cp '+before+'/'+str(i)+'/'+str(i)+'.nii.gz vertebral_labeling:/home/SCT/'
			command78='cd '+before+'/'+str(i)+' && '+'sudo docker cp '+before+'/'+str(i)+'/'+str(i)+'.nii.gz vertebral_labeling:/home/SCT/'	
			get_exit(command77, command78)
			command79='cd '+before+'/'+str(i)+' && '+'docker cp '+before+'/'+str(i)+'/'+str(i)+'_seg.nii.gz vertebral_labeling:/home/SCT/'
			command80='cd '+before+'/'+str(i)+' && '+'sudo docker cp '+before+'/'+str(i)+'/'+str(i)+'_seg.nii.gz vertebral_labeling:/home/SCT/'
			get_exit(command79, command80)
			command81='cd '+before+'/'+str(i)+' && '+'docker cp '+before+'/'+str(i)+'/'+str(i)+'_seg_labeled.nii.gz vertebral_labeling:/home/SCT/'
			command82='cd '+before+'/'+str(i)+' && '+'sudo docker cp '+before+'/'+str(i)+'/'+str(i)+'_seg_labeled.nii.gz vertebral_labeling:/home/SCT/'
			get_exit(command81, command82)
			command83='docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling python3 spine1.py'
			command84='sudo docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling python3 spine1.py'
			get_exit(command83, command84)
			command85='docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/'+str(i)+'_labels_vert.nii.gz'
			command86='sudo docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/'+str(i)+'_labels_vert.nii.gz'
			get_exit(command85, command86)
			command87='docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling python3 spine2.py'
			command88='sudo docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling python3 spine2.py'
			get_exit(command87, command88)
			command89='docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/anat2template.nii.gz'
			command90='sudo docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/anat2template.nii.gz'
			get_exit(command89, command90)
			command91='docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/straight_ref.nii.gz'
			command92='sudo docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/straight_ref.nii.gz'
			get_exit(command91, command92)
			command93='docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/template2anat.nii.gz'
			command94='sudo docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/template2anat.nii.gz'
			get_exit(command93, command94)
			command95='docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/warp_anat2template.nii.gz'
			command96='sudo docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/warp_anat2template.nii.gz'
			get_exit(command95, command96)
			command97='docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/warp_curve2straight.nii.gz'
			command98='sudo docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/warp_curve2straight.nii.gz'
			get_exit(command97, command98)
			command99='docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/warp_straight2curve.nii.gz'
			command100='sudo docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/warp_straight2curve.nii.gz'
			get_exit(command99, command100)
			command101='docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/warp_template2anat.nii.gz'
			command102='sudo docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/warp_template2anat.nii.gz'
			get_exit(command101, command102)
			command103='docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling python3 spine3.py'
			command104='sudo docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling python3 spine3.py'
			get_exit(command103, command104)
			command105='docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/label'
			command106='sudo docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/label'
			get_exit(command105, command106)
			command107='docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/straightening.cache'
			command108='sudo docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/straightening.cache'
			get_exit(command107, command108)
			command109='docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/qc_template_'+str(i)
			command110='sudo docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/qc_template_'+str(i)
			get_exit(command109, command110)
			command111='docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/qc_warp_'+str(i)
			command112='sudo docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling chmod -R 777 /home/SCT/qc_warp_'+str(i)
			get_exit(command111, command112)
			command113='docker cp vertebral_labeling:/home/SCT/anat2template.nii.gz '+before+'/'+str(i)+'/anat2template.nii.gz'
			command114='sudo docker cp vertebral_labeling:/home/SCT/anat2template.nii.gz '+before+'/'+str(i)+'/anat2template.nii.gz'		
			get_exit(command113, command114)
			command115='docker cp vertebral_labeling:/home/SCT/'+str(i)+'_labels_vert.nii.gz'+' '+before+'/'+str(i)+'/'+str(i)+'_labels_vert.nii.gz'
			command116='sudo docker cp vertebral_labeling:/home/SCT/'+str(i)+'_labels_vert.nii.gz'+' '+before+'/'+str(i)+'/'+str(i)+'_labels_vert.nii.gz'		
			get_exit(command115, command116)
			if 'label' in os.listdir(before+'/'+str(i)):
				shutil.rmtree(before+'/'+str(i)+'/label')
			command117='docker cp vertebral_labeling:/home/SCT/label '+before+'/'+str(i)+'/label'
			command118='sudo docker cp vertebral_labeling:/home/SCT/label '+before+'/'+str(i)+'/label'			
			get_exit(command117, command118)
			if 'qc_template_'+str(i) in os.listdir(before+'/'+str(i)):
				shutil.rmtree(before+'/'+str(i)+'/qc_template_'+str(i))
			command119='docker cp vertebral_labeling:/home/SCT/qc_template_'+str(i)+' '+before+'/'+str(i)+'/qc_template_'+str(i)
			command120='sudo docker cp vertebral_labeling:/home/SCT/qc_template_'+str(i)+' '+before+'/'+str(i)+'/qc_template_'+str(i)					
			get_exit(command119, command120)
			if 'qc_warp_'+str(i) in os.listdir(before+'/'+str(i)):
				shutil.rmtree(before+'/'+str(i)+'/qc_warp_'+str(i))
			command121='docker cp vertebral_labeling:/home/SCT/qc_warp_'+str(i)+' '+before+'/'+str(i)+'/qc_warp_'+str(i)
			command122='sudo docker cp vertebral_labeling:/home/SCT/qc_warp_'+str(i)+' '+before+'/'+str(i)+'/qc_warp_'+str(i)	
			get_exit(command121, command122)
			command123='docker cp vertebral_labeling:/home/SCT/straight_ref.nii.gz '+before+'/'+str(i)+'/straight_ref.nii.gz'
			command124='sudo docker cp vertebral_labeling:/home/SCT/straight_ref.nii.gz '+before+'/'+str(i)+'/straight_ref.nii.gz'		
			get_exit(command123, command124)
			command125='docker cp vertebral_labeling:/home/SCT/straightening.cache '+before+'/'+str(i)+'/straightening.cache'
			command126='sudo docker cp vertebral_labeling:/home/SCT/straightening.cache '+before+'/'+str(i)+'/straightening.cache'		
			get_exit(command125, command126)
			command127='docker cp vertebral_labeling:/home/SCT/template2anat.nii.gz '+before+'/'+str(i)+'/template2anat.nii.gz'
			command128='sudo docker cp vertebral_labeling:/home/SCT/template2anat.nii.gz '+before+'/'+str(i)+'/template2anat.nii.gz'	
			get_exit(command127, command128)
			command129='docker cp vertebral_labeling:/home/SCT/warp_anat2template.nii.gz '+before+'/'+str(i)+'/warp_anat2template.nii.gz'
			command130='sudo docker cp vertebral_labeling:/home/SCT/warp_anat2template.nii.gz '+before+'/'+str(i)+'/warp_anat2template.nii.gz'
			get_exit(command129, command130)
			command131='docker cp vertebral_labeling:/home/SCT/warp_curve2straight.nii.gz '+before+'/'+str(i)+'/warp_curve2straight.nii.gz'
			command132='sudo docker cp vertebral_labeling:/home/SCT/warp_curve2straight.nii.gz '+before+'/'+str(i)+'/warp_curve2straight.nii.gz'
			get_exit(command131, command132)
			command133='docker cp vertebral_labeling:/home/SCT/warp_straight2curve.nii.gz '+before+'/'+str(i)+'/warp_straight2curve.nii.gz'
			command134='sudo docker cp vertebral_labeling:/home/SCT/warp_straight2curve.nii.gz '+before+'/'+str(i)+'/warp_straight2curve.nii.gz'
			get_exit(command133, command134)
			command135='docker cp vertebral_labeling:/home/SCT/warp_template2anat.nii.gz '+before+'/'+str(i)+'/warp_template2anat.nii.gz'
			command136='sudo docker cp vertebral_labeling:/home/SCT/warp_template2anat.nii.gz '+before+'/'+str(i)+'/warp_template2anat.nii.gz'
			get_exit(command135, command136)
			command137='docker exec -it vertebral_labeling rm -rf /home/SCT/qc_template_'+str(i)
			command138='sudo docker exec -it vertebral_labeling rm -rf /home/SCT/qc_template_'+str(i)
			get_exit(command137, command138)
			command141='docker exec -it vertebral_labeling rm -rf /home/SCT/qc_warp_'+str(i)
			command142='sudo docker exec -it vertebral_labeling rm -rf /home/SCT/qc_warp_'+str(i)
			get_exit(command141, command142)
			command143='docker exec -it vertebral_labeling rm -rf /home/SCT/label'
			command144='sudo docker exec -it vertebral_labeling rm -rf /home/SCT/label'
			get_exit(command143, command144)
			command145='docker exec -it vertebral_labeling rm -f /home/SCT/anat2template.nii.gz'
			command146='sudo docker exec -it vertebral_labeling rm -f /home/SCT/anat2template.nii.gz'
			get_exit(command145, command146)
			command147='docker exec -it vertebral_labeling rm -f /home/SCT/straight_ref.nii.gz'
			command148='sudo docker exec -it vertebral_labeling rm -f /home/SCT/straight_ref.nii.gz'
			get_exit(command147, command148)
			command149='docker exec -it vertebral_labeling rm -f /home/SCT/straightening.cache'
			command150='sudo docker exec -it vertebral_labeling rm -f /home/SCT/straightening.cache'
			get_exit(command149, command150)
			command151='docker exec -it vertebral_labeling rm -f /home/SCT/template2anat.nii.gz'
			command152='sudo docker exec -it vertebral_labeling rm -f /home/SCT/template2anat.nii.gz'
			get_exit(command151, command152)
			command153='docker exec -it vertebral_labeling rm -f /home/SCT/warp_anat2template.nii.gz'
			command154='sudo docker exec -it vertebral_labeling rm -f /home/SCT/warp_anat2template.nii.gz'
			get_exit(command153, command154)
			command155='docker exec -it vertebral_labeling rm -f /home/SCT/warp_curve2straight.nii.gz'
			command156='sudo docker exec -it vertebral_labeling rm -f /home/SCT/warp_curve2straight.nii.gz'
			get_exit(command155, command156)
			command157='docker exec -it vertebral_labeling rm -f /home/SCT/warp_straight2curve.nii.gz'
			command158='sudo docker exec -it vertebral_labeling rm -f /home/SCT/warp_straight2curve.nii.gz'
			get_exit(command157, command158)
			command159='docker exec -it vertebral_labeling rm -f /home/SCT/warp_template2anat.nii.gz'
			command160='sudo docker exec -it vertebral_labeling rm -f /home/SCT/warp_template2anat.nii.gz'
			get_exit(command159, command160)
			command161='docker exec -it vertebral_labeling rm -f /home/SCT/'+str(i)+'.nii.gz'
			command162='sudo docker exec -it vertebral_labeling rm -f /home/SCT/'+str(i)+'.nii.gz'
			get_exit(command161, command162)
			command163='docker exec -it vertebral_labeling rm -f /home/SCT/'+str(i)+'_labels_vert.nii.gz'
			command164='sudo docker exec -it vertebral_labeling rm -f /home/SCT/'+str(i)+'_labels_vert.nii.gz'
			get_exit(command163, command164)
			command165='docker exec -it vertebral_labeling rm -f /home/SCT/'+str(i)+'_seg.nii.gz'
			command166='sudo docker exec -it vertebral_labeling rm -f /home/SCT/'+str(i)+'_seg.nii.gz'
			get_exit(command165, command166)
			command167='docker exec -it vertebral_labeling rm -f /home/SCT/'+str(i)+'_seg_labeled.nii.gz'
			command168='sudo docker exec -it vertebral_labeling rm -f /home/SCT/'+str(i)+'_seg_labeled.nii.gz'
			get_exit(command167, command168)		
	command169='docker stop vertebral_labeling'
	command170='sudo -S docker stop vertebral_labeling'
	exit190 = subprocess.run(command169, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
	if exit190 != 0:
		if password == None:
			password = get_pass()
		subprocess.run(command170, shell=True, check=True, input=password.encode())
	else:
		os.system(command169)
	command171='docker rm vertebral_labeling'
	command172='sudo -S docker rm vertebral_labeling'
	exit210 = subprocess.run(command171, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
	if exit210 != 0:
		if password == None:
			password = get_pass()
		subprocess.run(command172, shell=True, check=True, input=password.encode())
	else:
		os.system(command171)				
	print('\n')
	print('\033[92m\033[1mRESULTS:\033[0m')
	print('\n')
	def check_subfolders(directory, output_file_path):
		all_responses_are_one = True
		with open(output_file_path, 'w') as output_file:
			for subfolder in os.listdir(directory):
				if os.path.isdir(os.path.join(directory, subfolder)):
					if os.path.exists(os.path.join(directory, subfolder)+'/label/template/'):
						pass
					else:
						all_responses_are_one = False	
						print(f"\033[94m\033[1m{subfolder}\033[0m \033[93m\033[1mMISSING FOLDERS\033[0m")
						output_file.write(f"{subfolder} MISSING FOLDERS" + '\n')		
				subfolder_path = os.path.join(directory, subfolder)+'/label/template/'
				if os.path.isdir(subfolder_path):
					files = os.listdir(subfolder_path)
					if any('PAM50_levels.nii.gz' in file for file in files):
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[92m\033[1mOK\033[0m")
						output_file.write(f"{subfolder}.nii.gz OK" + '\n')
					elif not os.listdir(subfolder_path):
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}\033[0m \033[93m\033[1mMISSING FOLDERS\033[0m")
						output_file.write(f"{subfolder} MISSING FOLDERS" + '\n')												
					else:
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[91m\033[1mFAILED (MISSING REGISTRATION FILE)\033[0m")
						output_file.write(f"{subfolder}.nii.gz FAILED (MISSING REGISTRATION FILE)" + '\n')
                			
		if all_responses_are_one:
			print('\n')
			print("\033[92m\033[1mAUTOMATED REGISTRATION FINISHED\033[0m")
		else:
			print('\n')
			print("\033[93m\033[1mAUTOMATED REGISTRATION FINISHED WITH WARNINGS\033[0m")
	
	if not os.listdir(before):
		print('\n')
		print("\033[91m\033[1mREGISTRATION FAILED FAILED\033[0m")
	else:	      			
		check_subfolders(str(before), str(before)+'/AutomatedRegistrationResults.txt')	

#############################

def reg_aut_singularity():

	print('\033[94m\033[1mPLEASE TYPE THE PATH OF THE\033[0m \033[92m\033[1mEnigma-SC\033[0m \033[94m\033[1mFOLDER\033[0m')
	enigma_folder = input("Enigma-SC folder path: ")
	print('The \033[92m\033[1mEnigma-SC\033[0m folder selected is located at: '+enigma_folder)
	
	print('\033[94m\033[1mPLEASE TYPE THE PATH OF THE\033[0m \033[92m\033[1mPREPARED\033[0m \033[94m\033[1mFOLDER:\033[0m')
	file_paths = input("Prepared folder path: ")
	if not file_paths:
		print('\033[91m\033[1mNo folders selected.\033[0m')
		return
		
	print ('\033[92m\033[1mSelected files:\033[0m')
	path = str(file_paths)
	dir_list2 = os.listdir(path)
	for i in dir_list2:
		if '.txt' not in i:
			print(str(i)+'.nii.gz')
		
	before = str(file_paths)	

	exit_code = os.system("singularity --version")
	exity_code = os.system("apptainer --version")
	if exit_code and exity_code != 0:
    		print('\033[91m\033[1mSINGULARITY AND APPTAINER NOT INSTALLED. Please install one of them before running this script.\033[0m')
    		raise SystemExit(1)		
	
	k = os.listdir(enigma_folder+'/vertebral_labeling.simg/home/SCT/')
	for i in k:
		if os.path.isdir(enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)):
			shutil.rmtree(enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i))
		else:
			os.remove(enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i))		
	path = enigma_folder+'/vertebral_labeling.simg/home'
	dir_list = os.listdir(path)	
	for i in dir_list:
		if 'SCT' not in i:
			if 'datav2' not in i:
				if 'scripts' not in i:
					command21='rm -rf '+path+'/'+str(i)
					command22='sudo -S rm -rf '+path+'/'+str(i)
					exit2 = subprocess.run(command21, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
					if exit2 != 0:
						if password == None:
							password = get_pass()
						subprocess.run(command22, shell=True, check=True, input=password.encode('utf-8'))
					else:
						os.system(command21)				
		
	for i in dir_list2:
		if '.txt' not in i:
			if any(arq.endswith('.nii.gz') for arq in os.listdir('vertebral_labeling.simg/home/SCT/')):	
				command219='rm vertebral_labeling.simg/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/*nii.gz'
				command222='sudo -S rm vertebral_labeling.simg/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/*nii.gz'
				exit238 = subprocess.run(command219, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
				if exit238 != 0:
					if password == None:
						password = get_pass()
					subprocess.run(command222, shell=True, check=True, input=password.encode('utf-8'))
				else:
					os.system(command219)
			if any(arq.endswith('.cache') for arq in os.listdir('vertebral_labeling.simg/home/SCT/')):			
				command219='rm vertebral_labeling.simg/home/SCT/straightening.cache'
				command222='sudo -S rm vertebral_labeling.simg/home/SCT/straightening.cache'
				exit238 = subprocess.run(command219, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
				if exit238 != 0:
					if password == None:
						password = get_pass()
					subprocess.run(command222, shell=True, check=True, input=password.encode('utf-8'))
				else:
					os.system(command219)
			command171='cd '+before+'/'+str(i)+' && '+'cp '+before+'/'+str(i)+'/'+str(i)+'.nii.gz '+enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)+'.nii.gz'
			command172='cd '+before+'/'+str(i)+' && '+'sudo cp '+before+'/'+str(i)+'/'+str(i)+'.nii.gz '+enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)+'.nii.gz'
			get_exit(command171, command172)
			command173='chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)+'.nii.gz'
			command174='sudo chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)+'.nii.gz'
			try:
				subprocess.run(command173, shell=True, check=True)
			except subprocess.CalledProcessError as e:
				os.system(command174)				
			command175='cd '+before+'/'+str(i)+' && '+'cp '+before+'/'+str(i)+'/'+str(i)+'_seg.nii.gz '+enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)+'_seg.nii.gz'
			command176='cd '+before+'/'+str(i)+' && '+'sudo cp '+before+'/'+str(i)+'/'+str(i)+'_seg.nii.gz '+enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)+'_seg.nii.gz'
			get_exit(command175, command176)
			command177='chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)+'_seg.nii.gz'
			command178='sudo chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)+'_seg.nii.gz'
			try:
				subprocess.run(command177, shell=True, check=True)
			except subprocess.CalledProcessError as e:
				os.system(command178)	
			command179='cd '+before+'/'+str(i)+' && '+'sudo cp '+before+'/'+str(i)+'/'+str(i)+'_seg_labeled.nii.gz '+enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)+'_seg_labeled.nii.gz'
			command180='cd '+before+'/'+str(i)+' && '+'sudo cp '+before+'/'+str(i)+'/'+str(i)+'_seg_labeled.nii.gz '+enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)+'_seg_labeled.nii.gz'
			get_exit(command179, command180)
			command181='chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)+'_seg_labeled.nii.gz'
			command182='sudo chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)+'_seg_labeled.nii.gz'
			try:
				subprocess.run(command181, shell=True, check=True)
			except subprocess.CalledProcessError as e:
				os.system(command182)			
			cmd_1='singularity exec --writable --nv vertebral_labeling.simg/ python3 /spine1.py'
			cmd_11='sudo singularity exec --writable --nv vertebral_labeling.simg/ python3 /spine1.py'
			cmd_2='apptainer exec --writable --nv vertebral_labeling.simg/ python3 /spine1.py'
			cmd_22='sudo apptainer exec --writable --nv vertebral_labeling.simg/ python3 /spine1.py'
			exit3 = subprocess.run(cmd_1, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
			if exit3 != 0:
				cmd = cmd_11
			else:
				cmd = cmd_1
			try:		
				subprocess.run(cmd, shell=True, check=True)
			except subprocess.CalledProcessError:
				exit4 = subprocess.run(cmd_2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
				if exit4 != 0:
					cmd = cmd_22
				else:
					cmd = cmd_2	
				subprocess.run(cmd, shell=True, check=True)
			try:
				subprocess.run('chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)+'_labels_vert.nii.gz', shell=True, check=True)
			except subprocess.CalledProcessError as e:
				os.system('sudo chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/'+str(i)+'_labels_vert.nii.gz')	
			cmd_1='singularity exec --writable --nv vertebral_labeling.simg/ python3 /spine2.py'
			cmd_11='sudo singularity exec --writable --nv vertebral_labeling.simg/ python3 /spine2.py'
			cmd_2='apptainer exec --writable --nv vertebral_labeling.simg/ python3 /spine2.py'
			cmd_22='sudo apptainer exec --writable --nv vertebral_labeling.simg/ python3 /spine2.py'
			exit3 = subprocess.run(cmd_1, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
			if exit3 != 0:
				cmd = cmd_11
			else:
				cmd = cmd_1
			try:		
				subprocess.run(cmd, shell=True, check=True)
			except subprocess.CalledProcessError:
				exit4 = subprocess.run(cmd_2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
				if exit4 != 0:
					cmd = cmd_22
				else:
					cmd = cmd_2	
				subprocess.run(cmd, shell=True, check=True)
			try:
				subprocess.run('chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/anat2template.nii.gz',shell=True, check=True)
			except subprocess.CalledProcessError as e:
				os.system('sudo chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/anat2template.nii.gz')
			try:
				subprocess.run('chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/straight_ref.nii.gz', shell=True, check=True)
			except subprocess.CalledProcessError as e:
				os.system('sudo chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/straight_ref.nii.gz')
			try:		
				subprocess.run('chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/template2anat.nii.gz', shell=True, check=True)
			except subprocess.CalledProcessError as e:
				os.system('sudo chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/template2anat.nii.gz')
			try:	
				subprocess.run('chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/warp_anat2template.nii.gz', shell=True, check=True)
			except subprocess.CalledProcessError as e:
				os.system('sudo chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/warp_anat2template.nii.gz')
			try:		
				subprocess.run('chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/warp_curve2straight.nii.gz', shell=True, check=True)
			except subprocess.CalledProcessError as e:
				os.system('sudo chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/warp_curve2straight.nii.gz')
			try:	
				subprocess.run('chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/warp_straight2curve.nii.gz', shell=True, check=True)
			except subprocess.CalledProcessError as e:
				os.system('sudo chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/warp_straight2curve.nii.gz')
			try:	
				subprocess.run('chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/warp_template2anat.nii.gz', shell=True, check=True)
			except subprocess.CalledProcessError as e:
				os.system('sudo chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/warp_template2anat.nii.gz')
			cmd_1='singularity exec --writable --nv vertebral_labeling.simg/ python3 /spine3.py'
			cmd_11='sudo singularity exec --writable --nv vertebral_labeling.simg/ python3 /spine3.py'
			cmd_2='apptainer exec --writable --nv vertebral_labeling.simg/ python3 /spine3.py'
			cmd_22='sudo apptainer exec --writable --nv vertebral_labeling.simg/ python3 /spine3.py'
			exit3 = subprocess.run(cmd_1, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
			if exit3 != 0:
				cmd = cmd_11
			else:
				cmd = cmd_1
			try:		
				subprocess.run(cmd, shell=True, check=True)
			except subprocess.CalledProcessError:
				exit4 = subprocess.run(cmd_2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
				if exit4 != 0:
					cmd = cmd_22
				else:
					cmd = cmd_2	
				subprocess.run(cmd, shell=True, check=True)	
			try:
				subprocess.run('chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/label', shell=True, check=True)
			except subprocess.CalledProcessError as e:
				os.system('sudo chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/label')	
			try:
				subprocess.run('chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/straightening.cache', shell=True, check=True)
			except subprocess.CalledProcessError as e:
				os.system('sudo chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/straightening.cache')		
			try:	
				subprocess.run('chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/qc_template_'+str(i), shell=True, check=True)
			except subprocess.CalledProcessError as e:
				os.system('sudo chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/qc_template_'+str(i))	
			try:
				subprocess.run('chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/qc_warp_'+str(i), shell=True, check=True)
			except subprocess.CalledProcessError as e:
				os.system('sudo chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/SCT/qc_warp_'+str(i))
			try:
				subprocess.run('mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/anat2template.nii.gz '+before+'/'+str(i)+'/anat2template.nii.gz', shell=True, check=True)
			except subprocess.CalledProcessError as e:
				os.system('sudo mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/anat2template.nii.gz '+before+'/'+str(i)+'/anat2template.nii.gz')	
			try:
				os.system('mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/'+str(i)+'_labels_vert.nii.gz'+' '+before+'/'+str(i)+'/'+str(i)+'_labels_vert.nii.gz')
			except subprocess.CalledProcessError as e:
				os.system('sudo mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/'+str(i)+'_labels_vert.nii.gz'+' '+before+'/'+str(i)+'/'+str(i)+'_labels_vert.nii.gz')	
			if 'label' in os.listdir(before+'/'+str(i)):
				shutil.rmtree(before+'/'+str(i)+'/label')
			try:	
				os.system('mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/label'+' '+before+'/'+str(i)+'/label')
			except subprocess.CalledProcessError as e:
				os.system('sudo mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/label'+' '+before+'/'+str(i)+'/label')	
			if 'qc_template_'+str(i) in os.listdir(before+'/'+str(i)):
				shutil.rmtree(before+'/'+str(i)+'/qc_template_'+str(i))
			try:	
				os.system('mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/qc_template_'+str(i)+' '+before+'/'+str(i)+'/qc_template_'+str(i))
			except subprocess.CalledProcessError as e:
				os.system('sudo mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/qc_template_'+str(i)+' '+before+'/'+str(i)+'/qc_template_'+str(i))	
			if 'qc_warp_'+str(i) in os.listdir(before+'/'+str(i)):
				shutil.rmtree(before+'/'+str(i)+'/qc_warp_'+str(i))
			try:		
				os.system('mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/qc_warp_'+str(i)+' '+before+'/'+str(i)+'/qc_warp_'+str(i))
			except subprocess.CalledProcessError as e:
				os.system('sudo mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/qc_warp_'+str(i)+' '+before+'/'+str(i)+'/qc_warp_'+str(i))
			try:	
				os.system('mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/straight_ref.nii.gz '+before+'/'+str(i)+'/straight_ref.nii.gz')
			except subprocess.CalledProcessError as e:
				os.system('sudo mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/straight_ref.nii.gz '+before+'/'+str(i)+'/straight_ref.nii.gz')
			try:		
				os.system('mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/straightening.cache '+before+'/'+str(i)+'/straightening.cache')
			except subprocess.CalledProcessError as e:
				os.system('sudo mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/straightening.cache '+before+'/'+str(i)+'/straightening.cache')
			try:		
				os.system('mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/template2anat.nii.gz '+before+'/'+str(i)+'/template2anat.nii.gz')
			except subprocess.CalledProcessError as e:
				os.system('sudo mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/template2anat.nii.gz '+before+'/'+str(i)+'/template2anat.nii.gz')
			try:		
				os.system('mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/warp_anat2template.nii.gz '+before+'/'+str(i)+'/warp_anat2template.nii.gz')
			except subprocess.CalledProcessError as e:
				os.system('sudo mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/warp_anat2template.nii.gz '+before+'/'+ostr(i)+'/warp_anat2template.nii.gz')
			try:		
				os.system('mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/warp_curve2straight.nii.gz '+before+'/'+str(i)+'/warp_curve2straight.nii.gz')
			except subprocess.CalledProcessError as e:
				os.system('sudo mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/warp_curve2straight.nii.gz '+before+'/'+str(i)+'/warp_curve2straight.nii.gz')
			try:		
				os.system('mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/warp_straight2curve.nii.gz '+before+'/'+str(i)+'/warp_straight2curve.nii.gz')
			except subprocess.CalledProcessError as e:
				os.system('sudo mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/warp_straight2curve.nii.gz '+before+'/'+str(i)+'/warp_straight2curve.nii.gz')
			try:		
				os.system('mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/warp_template2anat.nii.gz '+before+'/'+str(i)+'/warp_template2anat.nii.gz')
			except subprocess.CalledProcessError as e:
				os.system('sudo mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/warp_template2anat.nii.gz '+before+'/'+str(i)+'/warp_template2anat.nii.gz')
			try:		
				os.system('rm '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/'+str(i)+'.nii.gz')
			except subprocess.CalledProcessError as e:
				os.system('sudo rm '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/'+str(i)+'.nii.gz')
			try:		
				os.system('rm '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/'+str(i)+'_seg.nii.gz')
			except subprocess.CalledProcessError as e:
				os.system('sudo rm '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/'+str(i)+'_seg.nii.gz')
			try:		
				os.system('rm '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/'+str(i)+'_seg_labeled.nii.gz')
			except subprocess.CalledProcessError as e:
				os.system('sudo rm '+enigma_folder+'/'+'vertebral_labeling.simg/home/SCT/'+str(i)+'_seg_labeled.nii.gz')								
	print('\n')
	print('\033[92m\033[1mRESULTS:\033[0m')
	print('\n')
	def check_subfolders(directory, output_file_path):
		all_responses_are_one = True
		with open(output_file_path, 'w') as output_file:
			for subfolder in os.listdir(directory):
				if os.path.isdir(os.path.join(directory, subfolder)):
					if os.path.exists(os.path.join(directory, subfolder)+'/label/template/'):
						pass
					else:
						all_responses_are_one = False	
						print(f"\033[94m\033[1m{subfolder}\033[0m \033[93m\033[1mMISSING FOLDERS\033[0m")
						output_file.write(f"{subfolder} MISSING FOLDERS" + '\n')		
				subfolder_path = os.path.join(directory, subfolder)+'/label/template/'
				if os.path.isdir(subfolder_path):
					files = os.listdir(subfolder_path)
					if any('PAM50_levels.nii.gz' in file for file in files):
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[92m\033[1mOK\033[0m")
						output_file.write(f"{subfolder}.nii.gz OK" + '\n')
					elif not os.listdir(subfolder_path):
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}\033[0m \033[93m\033[1mMISSING FOLDERS\033[0m")
						output_file.write(f"{subfolder} MISSING FOLDERS" + '\n')												
					else:
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[91m\033[1mFAILED (MISSING REGISTRATION FILE)\033[0m")
						output_file.write(f"{subfolder}.nii.gz FAILED (MISSING REGISTRATION FILE)" + '\n')
                			
		if all_responses_are_one:
			print('\n')
			print("\033[92m\033[1mAUTOMATED REGISTRATION FINISHED\033[0m")
		else:
			print('\n')
			print("\033[93m\033[1mAUTOMATED REGISTRATION FINISHED WITH WARNINGS\033[0m")
	
	if not os.listdir(before):
		print('\n')
		print("\033[91m\033[1mREGISTRATION FAILED FAILED\033[0m")
	else:	      			
		check_subfolders(str(before), str(before)+'/AutomatedRegistrationResults.txt')
#############################

def reg_man():
	
	print('\033[94m\033[1mPLEASE TYPE THE PATH OF THE PREPARED FOLDER.\033[0m \033[92m\033[1mUSE THE FOLDER CONTAINING ONLY THE FOLDERS\033[0m \033[94m\033[1m YOU RAN THE MANUAL VERTEBRAL LABELING STEP:\033[0m')
	file_paths = input("PATH OF THE FOLDER CONTAINING THE FOLDERS WHICH YOU RAN THE MANUAL VERTEBRAL LABELING STEP: ")
	if not file_paths:
		print('\033[91m\033[1mNo folders selected.\033[0m')
		return
		
	print ('\033[92m\033[1mSelected files:\033[0m')
	path = str(file_paths)
	dir_list = os.listdir(path)
	for i in dir_list:
		if '.txt' not in i:
			print(str(i)+'.nii.gz')
		
	before = str(file_paths)	
		
	for i in dir_list:
		if '.txt' not in i:
			if 'qc_template_manual_'+str(i) in os.listdir(before+'/'+str(i)):
				shutil.rmtree(before+'/'+str(i)+'/qc_template_manual_'+str(i))
			os.system('cd '+before+'/'+str(i)+' && sct_register_to_template -i '+str(i)+'.nii.gz'+' -s '+str(i)+'_seg.nii.gz -ldisc '+str(i)+'_labels_disc.nii.gz -c t1 -qc qc_template_manual_'+str(i))
	print('\n')
	print('\033[92m\033[1mRESULTS:\033[0m')
	print('\n')
	def check_subfolders(directory, output_file_path):
		all_responses_are_one = True
		with open(output_file_path, 'w') as output_file:
			for subfolder in os.listdir(directory):
				subfolder_path = os.path.join(directory, subfolder)
				if os.path.isdir(subfolder_path):
					files = os.listdir(subfolder_path)
					if any('qc_template_manual_' in file for file in files):
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[92m\033[1mOK\033[0m")
						output_file.write(f"{subfolder}.nii.gz OK" + '\n')						
					elif not os.listdir(subfolder_path):
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}\033[0m \033[93m\033[1mEMPTY FOLDER\033[0m")
						output_file.write(f"{subfolder} EMPTY FOLDER" + '\n')						
					else:
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[93m\033[1mNOT SELECTED\033[0m")
						output_file.write(f"{subfolder}.nii.gz NOT SELECTED" + '\n')
	
		if all_responses_are_one:
			print('\n')
			print("\033[92m\033[1mMANUAL REGISTRATION FINISHED\033[0m")
		else:
			print('\n')
			print("\033[93m\033[1mMANUAL REGISTRATION FINISHED WITH WARNINGS\033[0m")
	
	if not os.listdir(before):
		print('\n')
		print("\033[91m\033[1mMANUAL REGISTRATION FAILED\033[0m")
	else:	      			
		check_subfolders(str(before), str(before)+'/ManualRegistrationResults.txt')
	
		
#############################

def ext_docker():
	
	print('\033[94m\033[1mPLEASE TYPE THE PATH OF THE\033[0m \033[92m\033[1mPREPARED\033[0m \033[94m\033[1mFOLDER:\033[0m')
	file_paths = input("Prepared folder path: ")
	if not file_paths:
		print('\033[91m\033[1mNo folders selected.\033[0m')
		return
		
	print ('\033[92m\033[1mSelected files:\033[0m')
	path = str(file_paths)
	dir_list = os.listdir(path)
	for i in dir_list:
		if '.txt' not in i:
			print(str(i)+'.nii.gz')
		
	before = str(file_paths)
	
	data = ["subject", "CSA C1", "CSA C2", "CSA C3"]
	data2 = ["subject", "Mean(eccentricity) C1", "Mean(eccentricity) C2", "Mean(eccentricity) C3"]
	now = datetime.now()
	hour = str(now.strftime("%m-%d-%Y_%H-%M-%S"))
	csvf = before +'/csa_final_table_'+hour+'.csv'
	eccf = before +'/eccentricity_table'+hour+'.csv'
	
	with open(csvf, mode='w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(data)
	print('CSA final table saved on '+str(csvf))
	
	with open(eccf, mode='w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(data2)
	print('eccentricity final table saved on '+str(eccf))	

	exit_code = os.system("docker --version")
	if exit_code != 0:
    		print('\033[91m\033[1mDOCKER NOT INSTALLED. Please install Docker before running this script.\033[0m')
    		raise SystemExit(1)	
    	
	password = None	
		
	comando1='sudo -S docker stop vertebral_labeling'
	comando2='sudo -S docker rm vertebral_labeling'

	exit_code1 = subprocess.run('docker ps', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
	if exit_code1 != 0:
		if password == None:
			password = get_pass()	
		result = subprocess.check_output("sudo -S docker ps", shell=True, text=True, input=password)
		if 'vertebral_labeling' in result:
			subprocess.run(comando1, shell=True, check=True, input=password.encode('utf-8'))
			subprocess.run(comando2, shell=True, check=True, input=password.encode('utf-8'))
	else:
		result = subprocess.check_output("docker ps", shell=True, text=True)
		result = str(result)
		if 'vertebral_labeling' in result:
			os.system('docker stop vertebral_labeling')
			os.system('docker rm vertebral_labeling')
		
	exit_code2 = subprocess.run('docker ps -a', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
	if exit_code2 != 0:
		if password == None:
			password = get_pass()
		result = subprocess.check_output("sudo -S docker ps -a", shell=True, text=True, input=password)
		if 'vertebral_labeling' in result:
			subprocess.run(comando2, shell=True, check=True, input=password.encode('utf-8'))
	else:
		result = subprocess.check_output("docker ps", shell=True, text=True)
		result = str(result)
		if 'vertebral_labeling' in result:
			os.system('docker rm vertebral_labeling')																	
	try:
    		subprocess.run('nvidia-smi', check=True)
    		docker_command = 'docker run -itd --gpus all --ipc=host --name vertebral_labeling art2mri/vertebral_labeling:4.0'
	except FileNotFoundError as gpu_error:
    		print(f"Error checking for GPU: {gpu_error}")
    		docker_command = 'docker run -itd --ipc=host --name vertebral_labeling art2mri/vertebral_labeling:4.0'
	except subprocess.CalledProcessError as gpu_error:
    		print(f"Error checking for GPU: {gpu_error}")
    		docker_command = 'docker run -itd --ipc=host --name vertebral_labeling art2mri/vertebral_labeling:4.0'	
	try:
    		subprocess.run(docker_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
	except subprocess.CalledProcessError as docker_error:
		if password == None:
			password = get_pass()
		subprocess.run('sudo -S '+docker_command2, shell=True, check=True, input=password.encode('utf-8'))	
		print(f"Error running Docker command: {docker_error}")
    		   		    			
	loww1='docker run -itd --gpus all --ipc=host --name vertebral_labeling art2mri/vertebral_labeling:4.0'
	loww2='sudo -S docker run -itd --gpus all --ipc=host --name vertebral_labeling art2mri/vertebral_labeling:4.0'
	try:
		subprocess.run(loww1, shell=True, check=True, stderr=subprocess.DEVNULL)
	except subprocess.CalledProcessError as e:
			if password == None:
				password = get_pass()
			subprocess.run(loww2, shell=True, check=True, input=password.encode('utf-8'))			
	
	for i in dir_list:
		if '.txt' not in i:
			v = []
			k = []
			b1 = []
			try:
				subprocess.run('docker start vertebral_labeling', shell=True, check=True, stderr=subprocess.DEVNULL)
			except subprocess.CalledProcessError as e:
				if password == None:
					password = get_pass()
				subprocess.run('sudo -S docker start vertebral_labeling', shell=True, check=True, input=password.encode())
			
			command183='docker cp '+before+'/'+str(i)+' vertebral_labeling:/home/'+str(i)
			command184='sudo docker cp '+before+'/'+str(i)+' vertebral_labeling:/home/'+str(i)			
			get_exit(command183, command184)
			command185='docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling python3 spine4.py'
			command186='sudo docker exec -e SCT_DIR=''/spinalcordtoolbox'' -e PATH=''/spinalcordtoolbox/bin:$PATH'' -it vertebral_labeling python3 spine4.py'
			get_exit(command185, command186)
			command187='docker exec -it vertebral_labeling chmod -R 777 /home/'+str(i)+'/'+str(i)+'_csa.csv'
			command188='sudo docker exec -it vertebral_labeling chmod -R 777 /home/'+str(i)+'/'+str(i)+'_csa.csv'
			get_exit(command187, command188)
			command189='docker cp vertebral_labeling:/home/'+str(i)+'/'+str(i)+'_csa.csv'+' '+before+'/'+str(i)+'/'+str(i)+'_csa.csv'
			command190='sudo docker cp vertebral_labeling:/home/'+str(i)+'/'+str(i)+'_csa.csv'+' '+before+'/'+str(i)+'/'+str(i)+'_csa.csv'
			get_exit(command189, command190)
			command191='docker exec -it vertebral_labeling rm -r /home/'+str(i)
			command192='sudo docker exec -it vertebral_labeling rm -r /home/'+str(i)
			get_exit(command191, command192)
			with open(before+'/'+str(i)+'/'+str(i)+'_csa.csv', 'r', encoding='utf-8') as file:
				sp = csv.reader(file)
				for row in sp:
					v.append(row)		
			k.append(str(i))
			b1.append(str(i))		
			for j in range(len(v)):
				if v[j][4] == '1':
					f = j
					w = ((float(v[f][6])*math.cos((math.radians(float(v[f][8]))))+((float(v[f][6]))*math.cos(math.radians(float(v[f][10]))))))/(2)
					k.append(str(w))
					b1.append(str(v[f][16]))
			for j in range(len(v)):		
				if v[j][4] == '2':
					f = j
					w = ((float(v[f][6])*math.cos((math.radians(float(v[f][8]))))+((float(v[f][6]))*math.cos(math.radians(float(v[f][10]))))))/(2)
					k.append(str(w))
					b1.append(str(v[f][16]))
			for j in range(len(v)):
				if v[j][4] == '3':
					f = j
					w = ((float(v[f][6])*math.cos((math.radians(float(v[f][8]))))+((float(v[f][6]))*math.cos(math.radians(float(v[f][10]))))))/(2)
					k.append(str(w))
					b1.append(str(v[f][16]))
			with open(csvf, 'a', newline='') as csv_file:
				writer = csv.writer(csv_file)
				writer.writerow(k)
			with open(eccf, 'a', newline='') as csv_file:
				writer = csv.writer(csv_file)
				writer.writerow(b1)
			
	command17='docker stop vertebral_labeling'
	command18='sudo -S docker stop vertebral_labeling'
	exit9 = subprocess.run(command17, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
	if exit9 != 0:
		if password == None:
			password = get_pass()
		subprocess.run(command18, shell=True, check=True, input=password.encode())
	else:
		os.system(command17)
	command19='docker rm vertebral_labeling'
	command20='sudo -S docker rm vertebral_labeling'
	exit10 = subprocess.run(command19, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
	if exit10 != 0:
		if password == None:
			password = get_pass()
		subprocess.run(command20, shell=True, check=True, input=password.encode())
	else:
		os.system(command19)					
	print('\n')
	print('\033[92m\033[1mRESULTS:\033[0m')
	print('\n')
	def check_subfolders(directory, output_file_path):
		all_responses_are_one = True
		with open(output_file_path, 'w') as output_file:
			for subfolder in os.listdir(directory):
				subfolder_path = os.path.join(directory, subfolder)
				if os.path.isdir(subfolder_path):
					files = os.listdir(subfolder_path)
					if any('_csa.csv' in file for file in files):
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[92m\033[1mOK\033[0m")
						output_file.write(f"{subfolder}.nii.gz OK" + '\n')						
					elif not os.listdir(subfolder_path):
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}\033[0m \033[93m\033[1mEMPTY FOLDER\033[0m")
						output_file.write(f"{subfolder} EMPTY FOLDER" + '\n')						
					else:
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[91m\033[1mFAILED (MISSING EXTRACTION FILE .csv)\033[0m")
						output_file.write(f"{subfolder}.nii.gz FAILED (MISSING EXTRACTION FILE .csv)" + '\n')
                			
		if all_responses_are_one:
			print('\n')
			print("\033[92m\033[1mDATA EXTRACTION FINISHED\033[0m")
		else:
			print('\n')
			print("\033[93m\033[1mDATA EXTRACTION FINISHED WITH WARNINGS\033[0m")
	
	if not os.listdir(before):
		print('\n')
		print("\033[91m\033[1mDATA EXTRACTION FAILED\033[0m")
	else:	      			
		check_subfolders(str(before), str(before)+'/DataExtractionResults.txt')	

#############################	

def ext_singularity():
	print('\033[94m\033[1mPLEASE TYPE THE PATH OF THE\033[0m \033[92m\033[1mEnigma-SC\033[0m \033[94m\033[1mFOLDER\033[0m')
	enigma_folder = input("Enigma-SC folder path: ")
	print('The \033[92m\033[1mEnigma-SC\033[0m folder selected is located at: '+enigma_folder)
	
	print('\033[94m\033[1mPLEASE TYPE THE PATH OF THE\033[0m \033[92m\033[1mPREPARED\033[0m \033[94m\033[1mFOLDER:\033[0m')
	file_paths = input("Prepared folder path: ")
	if not file_paths:
		print('\033[91m\033[1mNo folders selected.\033[0m')
		return
		
	print ('\033[92m\033[1mSelected files:\033[0m')
	path = str(file_paths)
	dir_list2 = os.listdir(path)
	for i in dir_list2:
		if '.txt' not in i:
			print(str(i)+'.nii.gz')
		
	before = str(file_paths)
	
	data = ["subject", "CSA C1", "CSA C2", "CSA C3"]
	data2 = ["subject", "Mean(eccentricity) C1", "Mean(eccentricity) C2", "Mean(eccentricity) C3"]
	now = datetime.now()
	hour = str(now.strftime("%m-%d-%Y_%H-%M-%S"))
	csvf = before +'/csa_final_table_'+hour+'.csv'
	eccf = before +'/eccentricity_table'+hour+'.csv'
	
	with open(csvf, mode='w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(data)
	print('CSA final table saved on '+str(csvf))
	
	with open(eccf, mode='w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(data2)
	print('eccentricity final table saved on '+str(eccf))	
	
	path = enigma_folder+'/vertebral_labeling.simg/home'
	dir_list = os.listdir(path)
	for i in dir_list:
		if 'SCT' not in i:
			if 'datav2' not in i:
				if 'scripts' not in i:
					command21='rm -rf '+path+'/'+str(i)
					command22='sudo rm -rf '+path+'/'+str(i)
					get_exit(command21, command22)
		
	exit_code = os.system("singularity --version")
	exity_code = os.system("apptainer --version")
	if exit_code and exity_code != 0:
    		print('\033[91m\033[1mSINGULARITY AND APPTAINER NOT INSTALLED. Please install on of them before running this script.\033[0m')
    		raise SystemExit(1)		
				
	for i in dir_list2:
		if '.txt' not in i:
			v = []
			k = []
			b1 = []
			try:
				subprocess.run ('cd '+before+'/'+str(i)+' && '+'cp -r '+before+'/'+str(i)+' '+enigma_folder+'/vertebral_labeling.simg/home/'+str(i),  shell=True)
			except subprocess.CalledProcessError as e:
				os.system('cd '+before+'/'+str(i)+' && '+'sudo cp -r '+before+'/'+str(i)+' '+enigma_folder+'/vertebral_labeling.simg/home/'+str(i), shell=True)	
			try:		
				subprocess.run('sudo singularity exec --writable vertebral_labeling.simg/ python3 /spine4.py', shell=True, check=True)
			except subprocess.CalledProcessError:
				subprocess.run('sudo apptainer exec --writable vertebral_labeling.simg/ python3 /spine4.py', shell=True, check=True)
			
			cmd_1='singularity exec --writable vertebral_labeling.simg/ python3 /spine4.py'
			cmd_11='sudo singularity exec --writable vertebral_labeling.simg/ python3 /spine4.py'
			cmd_2='apptainer exec --writable --nv vertebral_labeling.simg/ python3 /spine4.py'
			cmd_22='sudo apptainer exec --writable --nv vertebral_labeling.simg/ python3 /spine4.py'
			exit3 = subprocess.run(cmd_1, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
			if exit3 != 0:
				cmd = cmd_11
			else:
				cmd = cmd_1
			try:		
				subprocess.run(cmd, shell=True, check=True)
			except subprocess.CalledProcessError:
				exit4 = subprocess.run(cmd_2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
				if exit4 != 0:
					cmd = cmd_22
				else:
					cmd = cmd_2	
				subprocess.run(cmd, shell=True, check=True)				
			try:			
				subprocess.run('chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/'+str(i)+'/'+str(i)+'_csa.csv', shell=True, check=True)
			except subprocess.CalledProcessError as e:
				os.system('sudo chmod -R 777 '+enigma_folder+'/vertebral_labeling.simg/home/'+str(i)+'/'+str(i)+'_csa.csv')	
			try:	
				os.system('mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/'+str(i)+'/'+str(i)+'_csa.csv'+' '+before+'/'+str(i)+'/'+str(i)+'_csa.csv')
			except subprocess.CalledProcessError as e:
				os.system('sudo mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/'+str(i)+'/'+str(i)+'_csa.csv'+' '+before+'/'+str(i)+'/'+str(i)+'_csa.csv')
			cmdd_1='singularity exec --writable --nv vertebral_labeling.simg/ rm -rf /home/'+str(i)
			cmdd_11='sudo singularity exec --writable --nv vertebral_labeling.simg/ rm -rf /home/'+str(i)
			cmdd_2='apptainer exec --writable --nv vertebral_labeling.simg/ rm -rf /home/'+str(i)
			cmdd_22='sudo apptainer exec --writable --nv vertebral_labeling.simg/ rm -rf /home/'+str(i)
			exit4 = subprocess.run(cmdd_1, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
			if exit4 != 0:
				cmdd = cmdd_11
			else:
				cmdd = cmdd_1
			try:		
				subprocess.run(cmdd, shell=True, check=True)
			except subprocess.CalledProcessError:
				exit4 = subprocess.run(cmdd_2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
				if exit4 != 0:
					cmdd = cmdd_22
				else:
					cmdd = cmdd_2	
				subprocess.run(cmdd, shell=True, check=True)					
			with open(before+'/'+str(i)+'/'+str(i)+'_csa.csv', 'r', encoding='utf-8') as file:
				sp = csv.reader(file)
				for row in sp:
					v.append(row)		
			k.append(str(i))
			b1.append(str(i))		
			for j in range(len(v)):
				if v[j][4] == '1':
					f = j
					w = ((float(v[f][6])*math.cos((math.radians(float(v[f][8]))))+((float(v[f][6]))*math.cos(math.radians(float(v[f][10]))))))/(2)
					k.append(str(w))
					b1.append(str(v[f][16]))
			for j in range(len(v)):		
				if v[j][4] == '2':
					f = j
					w = ((float(v[f][6])*math.cos((math.radians(float(v[f][8]))))+((float(v[f][6]))*math.cos(math.radians(float(v[f][10]))))))/(2)
					k.append(str(w))
					b1.append(str(v[f][16]))
			for j in range(len(v)):
				if v[j][4] == '3':
					f = j
					w = ((float(v[f][6])*math.cos((math.radians(float(v[f][8]))))+((float(v[f][6]))*math.cos(math.radians(float(v[f][10]))))))/(2)
					k.append(str(w))
					b1.append(str(v[f][16]))
			with open(csvf, 'a', newline='') as csv_file:
				writer = csv.writer(csv_file)
				writer.writerow(k)
			with open(eccf, 'a', newline='') as csv_file:
				writer = csv.writer(csv_file)
				writer.writerow(b1)				
	print('\n')
	print('\033[92m\033[1mRESULTS:\033[0m')
	print('\n')
	def check_subfolders(directory, output_file_path):
		all_responses_are_one = True
		with open(output_file_path, 'w') as output_file:
			for subfolder in os.listdir(directory):
				subfolder_path = os.path.join(directory, subfolder)
				if os.path.isdir(subfolder_path):
					files = os.listdir(subfolder_path)
					if any('_csa.csv' in file for file in files):
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[92m\033[1mOK\033[0m")
						output_file.write(f"{subfolder}.nii.gz OK" + '\n')						
					elif not os.listdir(subfolder_path):
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}\033[0m \033[93m\033[1mEMPTY FOLDER\033[0m")
						output_file.write(f"{subfolder} EMPTY FOLDER" + '\n')						
					else:
						all_responses_are_one = False
						print(f"\033[94m\033[1m{subfolder}.nii.gz\033[0m \033[91m\033[1mFAILED (MISSING EXTRACTION FILE .csv)\033[0m")
						output_file.write(f"{subfolder}.nii.gz FAILED (MISSING EXTRACTION FILE .csv)" + '\n')
                			
		if all_responses_are_one:
			print('\n')
			print("\033[92m\033[1mDATA EXTRACTION FINISHED\033[0m")
		else:
			print('\n')
			print("\033[93m\033[1mDATA EXTRACTION FINISHED WITH WARNINGS\033[0m")
	
	if not os.listdir(before):
		print('\n')
		print("\033[91m\033[1mDATA EXTRACTION FAILED\033[0m")
	else:	      			
		check_subfolders(str(before), str(before)+'/DataExtractionResults.txt')	
		
#############################	

def pack():
	print('\033[94m\033[1mPLEASE TYPE THE PATH OF THE\033[0m \033[92m\033[1mPREPARED\033[0m \033[94m\033[1mFOLDER:\033[0m')
	file_paths = input("Prepared folder path: ")
	if not file_paths:
		print('\033[91m\033[1mNo folders selected.\033[0m')
		return
		
	print ('\033[92m\033[1mSelected files:\033[0m')
	path = str(file_paths)
	dir_list = os.listdir(path)
	for i in dir_list:
		if '.txt' not in i:
			if '.csv' not in i:
				print(str(i)+'.nii.gz')
		
	before = str(file_paths)
	
	for i in dir_list:
		if '.txt' not in i:
			if '.csv' not in i:
				os.system('cd '+str(before)+' && zip -r '+str(i)+'.zip'+' '+str(i)+' -x '+str(i)+'/'+str(i)+'.nii.gz')	
	print ('\033[92m\033[1mDATA PACKED AND READY TO GO!\033[0m')
	print ('\033[94m\033[1mZIP files located at: '+str(before)+'\033[0m')		
			
         
#############################

def open_tutorial():
    url = "https://github.com/art2mri/Enigma-SC" 
    webbrowser.open_new(url)
    
#############################	

while True:
	print("\n\033[94m\033[1mYOU ARE NOW RUNNING THE\033[0m \033[92m\033[1mEnigma-SC\033[0m \033[94m\033[1mPIPELINE\033[0m\n")
	print("\033[94m\033[1mPLEASE CHOOSE A COMMAND:\033[0m\n")
	print("\033[92m\033[1m1.\033[0m Prepare Folders")
	print("\033[92m\033[1m2.\033[0m Spinal Cord Segmentation")
	print("\033[92m\033[1m3.\033[0m Automated Vertebral Labeling")
	print("\033[93m\033[1m4.\033[0m Manual Vertebral Labeling")
	print("\033[92m\033[1m5.\033[0m Automated Spinal Cord Registration")
	print("\033[93m\033[1m6.\033[0m Manual Spinal Cord Registration")
	print("\033[92m\033[1m7.\033[0m Data Extraction")
	print("\033[92m\033[1m8.\033[0m Pack and Send")
	print("\033[93m\033[1m9.\033[0m Tutorial")
	print("\033[91m\033[1m0.\033[0m Exit\n")

	while True:
		command = input("Type your choice: ")

		if command in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
			break 
		else:
			print('\033[91m\033[1mInvalid choice. Please enter a number from 0 to 9.\033[0m')

	if command == "1":
		while True:
			print('\n')
			print("\033[92m\033[1mPREPARE FOLDERS \033[0m")
			print("\033[94m\033[1mSelect the input format: \033[0m")
			print("\033[92m\033[1m1.\033[0m .nii.gz files")
			print("\033[92m\033[1m2.\033[0m BIDS dataset")
			print("\033[91m\033[1m0.\033[0m Return\n")
			commando = input("Type your choice: ")
			if commando in ["0", "1", "2"]:
				if commando == "0":
					break  
				if commando == "1":
					browse_folder_niigz()
					break
				if commando == "2":
					browse_folder_BIDS()
					break
			else:			
				print('\033[91m\033[1mInvalid choice. Please enter a number from 1 to 2.\033[0m')

            		
	elif command == "2":
		while True:
			print('\n')
			print("\033[92m\033[1mSPINAL CORD SEGMENTATION \033[0m")
			print("\033[94m\033[1mSelect platform: \033[0m")
			print("\033[92m\033[1m1.\033[0m Docker")
			print("\033[92m\033[1m2.\033[0m Singularity/Apptainer")
			print("\033[91m\033[1m0.\033[0m Return\n")
			commando = input("Type your choice: ")
			if commando in ["0", "1", "2"]:
				if commando == "0":
					break  
				if commando == "1":
					modal_docker()
					break
				if commando == "2":
					modal_singularity()
					break
			else:			
				print('\033[91m\033[1mInvalid choice. Please enter a number from 1 to 2.\033[0m')			
	elif command == "3":
		while True:
			print('\n')
			print("\033[92m\033[1mAUTOMATED VERTEBRAL LABELING \033[0m")
			print("\033[94m\033[1mSelect platform: \033[0m")
			print("\033[92m\033[1m1.\033[0m Docker")
			print("\033[92m\033[1m2.\033[0m Singularity/Apptainer")
			print("\033[91m\033[1m0.\033[0m Return\n")
			commando = input("Type your choice: ")
			if commando in ["0", "1", "2"]:
				if commando == "0":
					break  
				if commando == "1":
					docker()
					break
				if commando == "2":
					singularity()
					break
			else:			
				print('\033[91m\033[1mInvalid choice. Please enter a number from 1 to 2.\033[0m')
	elif command == "4":
		while True:
			print('\n')
			print("\033[92m\033[1mMANUAL VERTEBRAL LABELING (REQUIERES THE SPINAL CORD TOOLBOX INSTALLATION (https://spinalcordtoolbox.com/) - RUN THIS COMMAND ONLY FOR THOSE IMAGES WHICH FAILED ON THE AUTOMATED VERTEBRAL LABELING STEP)\033[0m")
			print("\033[94m\033[1mSelect platform: \033[0m")
			print("\033[92m\033[1m1.\033[0m Docker")
			print("\033[92m\033[1m2.\033[0m Singularity/Apptainer")
			print("\033[91m\033[1m0.\033[0m Return\n")
			commando = input("Type your choice: ")
			if commando in ["0", "1", "2"]:
				if commando == "0":
					break  
				if commando == "1":
					manual()
					break
				if commando == "2":
					manual()
					break
			else:			
				print('\033[91m\033[1mInvalid choice. Please enter a number from 1 to 2.\033[0m')
	elif command == "5":
		while True:
			print('\n')
			print("\033[92m\033[1mAUTOMATED SPINAL CORD REGISTRATION\033[0m")
			print("\033[94m\033[1mSelect platform: \033[0m")
			print("\033[92m\033[1m1.\033[0m Docker")
			print("\033[92m\033[1m2.\033[0m Singularity/Apptainer")
			print("\033[91m\033[1m0.\033[0m Return\n")
			commando = input("Type your choice: ")
			if commando in ["0", "1", "2"]:
				if commando == "0":
					break  
				if commando == "1":
					reg_aut_docker()
					break
				if commando == "2":
					reg_aut_singularity()
					break
			else:			
				print('\033[91m\033[1mInvalid choice. Please enter a number from 1 to 2.\033[0m')
	elif command == "6":
		while True:
			print('\n')
			print("\033[92m\033[1mMANUAL SPINAL CORD REGISTRATION (REQUIERES THE SPINAL CORD TOOLBOX INSTALLATION (https://spinalcordtoolbox.com/) - RUN THIS COMMAND ONLY FOR THOSE IMAGES WHICH FAILED ON THE AUTOMATED VERTEBRAL LABELING STEP)\033[0m")
			print("\033[94m\033[1mSelect platform: \033[0m")
			print("\033[92m\033[1m1.\033[0m Docker")
			print("\033[92m\033[1m2.\033[0m Singularity/Apptainer")
			print("\033[91m\033[1m0.\033[0m Return\n")
			commando = input("Type your choice: ")
			if commando in ["0", "1", "2"]:
				if commando == "0":
					break  
				if commando == "1":
					reg_man()
					break
				if commando == "2":
					reg_man()
					break
			else:			
				print('\033[91m\033[1mInvalid choice. Please enter a number from 1 to 2.\033[0m')
	elif command == "7":
		while True:
			print('\n')
			print("\033[92m\033[1mDATA EXTRACTION\033[0m")
			print("\033[94m\033[1mSelect platform: \033[0m")
			print("\033[92m\033[1m1.\033[0m Docker")
			print("\033[92m\033[1m2.\033[0m Singularity/Apptainer")
			print("\033[91m\033[1m0.\033[0m Return\n")
			commando = input("Type your choice: ")
			if commando in ["0", "1", "2"]:
				if commando == "0":
					break  
				if commando == "1":
					ext_docker()
					break
				if commando == "2":
					ext_singularity()
					break
			else:			
				print('\033[91m\033[1mInvalid choice. Please enter a number from 1 to 2.\033[0m')
	elif command == "8":
		while True:
			print('\n')
			print("\033[92m\033[1mPACK AND SEND\033[0m")
			print("\033[94m\033[1mSelect platform: \033[0m")
			print("\033[92m\033[1m1.\033[0m Docker")
			print("\033[92m\033[1m2.\033[0m Singularity/Apptainer")
			print("\033[91m\033[1m0.\033[0m Return\n")
			commando = input("Type your choice: ")
			if commando in ["0", "1", "2"]:
				if commando == "0":
					break  
				if commando == "1":
					pack()
					break
				if commando == "2":
					pack()
					break
			else:			
				print('\033[91m\033[1mInvalid choice. Please enter a number from 1 to 2.\033[0m')
	elif command == "9":
		open_tutorial()
		break
	elif command == "0":
		print("Exiting the Enigma-SC pipeline.")
		break






