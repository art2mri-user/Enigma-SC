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
import tkfilebrowser
import csv
import math
import tkinter as tk
import webbrowser
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import simpledialog
from datetime import datetime

from tkinter import ttk
import shutil

#############################

def browse_folder():
	root = tk.Tk()
	root.withdraw()	
	
	file_paths = filedialog.askopenfilenames(
		title="Select Files",
		filetypes=[("All Files","*.*")]
	)
	
	if not file_paths:
		print('\033[91m\033[1mNo files selected.\033[0m')
		return
		
	print ('\033[92m\033[1mSelected files:\033[0m')
	for file_path in file_paths:
		print(file_path)
		if 'nii.gz' not in os.path.basename(str(file_path)):
			os.system('gzip '+ file_path)
		
	before = str(file_paths[0])
	before = os.path.dirname(before)
	
	progress_window = tk.Toplevel()
	progress_window.title("Preparing Folders Progress")

	progress_label = tk.Label(progress_window, text="Preparing...")
	progress_label.pack()

	progress_bar = ttk.Progressbar(progress_window, length=300, mode="determinate")
	progress_bar.pack()

	progress_text = tk.Label(progress_window, text="")
	progress_text.pack()
	
	def update_progress_bar(current, total):
		progress_percent = int((current / total) * 99)
		progress_bar["value"] = progress_percent
		progress_text["text"] = f"{progress_percent}% done"
		progress_window.update()
	
	os.system('cd '+ before + ' && '+ 'cd ..'+' && '+ 'mkdir spine')
	command = 'cd '+before+' && '+'cd ..'+' && '+'cd spine' +' && '+'pwd'	
	output = os.popen(command).read().strip()
	for idx,i in enumerate(file_paths):
		update_progress_bar(idx + 1, len(file_paths))
		if '.nii.gz' in i:
			os.system('cd '+before+' && '+ 'cd ..'+' && '+ 'cd spine'+ ' && '+ 'mkdir ' +os.path.basename(str(i)).replace(".nii.gz",""))
			os.system('cp '+str(i)+' '+str(output)+'/'+os.path.basename(str(i)).replace(".nii.gz","")+'/'+os.path.basename(str(i)))
		if '.gz' not in i:
			os.system('cd '+before+' && '+ 'cd ..'+' && '+ 'cd spine'+ ' && '+ 'mkdir ' +os.path.basename(str(i)).replace(".nii",""))
			os.system('cp '+str(i)+' '+str(output)+'/'+os.path.basename(str(i)).replace(".nii","")+'/'+os.path.basename(str(i).replace(".nii",".nii.gz")))								
		if '.nii' not in i:
			os.system(os.path.basename(str(i))+'\033[91m\033[1m is not a .nii or .nii.gz file\033[0m')
	progress_label.config(text="FOLDERS PREPARED!")
	progress_window.update()
	progress_window.after(4000, progress_window.destroy)		
	print('\033[92m\033[1mFOLDERS PREPARED!\033[0m')		
                     
        
#############################   

def modal_1():			 			 	       	
	file_paths = tkfilebrowser.askopendirnames()
	
	if not file_paths:
		print('\033[91m\033[1mNo folders selected.\033[0m')
		return
		
	print ('\033[92m\033[1mSelected folders:\033[0m')
	for file_path in file_paths:
		print(file_path)
		
	before = str(file_paths[0])
	before = os.path.dirname(before)	
           	            	 		
	command = 'cd '+before+' && '+'cd ..'+' && '+'cd spine' +' && '+'pwd'	
	output = os.popen(command).read().strip() 
	
	progress_window = tk.Toplevel()
	progress_window.title("Segmentation Progress")

	progress_label = tk.Label(progress_window, text="Segmenting...")
	progress_label.pack()

	progress_bar = ttk.Progressbar(progress_window, length=300, mode="determinate")
	progress_bar.pack()

	progress_text = tk.Label(progress_window, text="")
	progress_text.pack()
	
	def update_progress_bar(current, total):
		progress_percent = int((current / total) * 99)
		progress_bar["value"] = progress_percent
		progress_text["text"] = f"{progress_percent}% done"
		progress_window.update()
    	 
	for idx, i in enumerate(file_paths): 
		update_progress_bar(idx + 1, len(file_paths))
		os.system ('cd '+output+'/'+os.path.basename(str(i).replace(".nii.gz","")))
		os.system ('cd '+output+'/'+os.path.basename(str(i).replace(".nii.gz",""))+' && '+'sct_deepseg_sc -i '+os.path.basename(str(i).replace(".nii.gz",""))+'.nii.gz'+' -c t1 -qc qc_'+os.path.basename(str(i).replace(".nii.gz","")).replace(".nii",""))
	progress_label.config(text="SEGMENTATION FINISHED!")
	progress_window.update()
	progress_window.after(4000, progress_window.destroy)	
	print('\033[92m\033[1mSEGMENTATION FINISHED!\033[0m')    

#############################  

def docker():
	file_paths = tkfilebrowser.askopendirnames()
	
	if not file_paths:
		print('\033[91m\033[1mNo folders selected.\033[0m')
		return
		
	print ('\033[92m\033[1mSelected folders:\033[0m')
	for file_path in file_paths:
		print(file_path)
		
	progress_window = tk.Toplevel()
	progress_window.title("Automated Labeling Progress")

	progress_label = tk.Label(progress_window, text="Labeling...")
	progress_label.pack()

	progress_bar = ttk.Progressbar(progress_window, length=300, mode="determinate")
	progress_bar.pack()

	progress_text = tk.Label(progress_window, text="")
	progress_text.pack()
	
	def update_progress_bar(current, total):
		progress_percent = int((current / total) * 99)
		progress_bar["value"] = progress_percent
		progress_text["text"] = f"{progress_percent}% done"
		progress_window.update()	
		
	os.system('sudo docker stop vertebral_labeling')
	os.system('sudo docker rm vertebral_labeling')
	
	try:
    		subprocess.run('nvidia-smi', check=True)
    		docker_command = 'sudo docker run -itd --gpus all --ipc=host --name vertebral_labeling art2mri/vertebral_labeling:2.0'
	except FileNotFoundError as gpu_error:
    		print(f"Error checking for GPU: {gpu_error}")
    		docker_command = 'sudo docker run -itd --ipc=host --name vertebral_labeling art2mri/vertebral_labeling:2.0'
	except subprocess.CalledProcessError as gpu_error:
    		print(f"Error checking for GPU: {gpu_error}")
    		docker_command = 'sudo docker run -itd --ipc=host --name vertebral_labeling art2mri/vertebral_labeling:2.0'

	try:
    		subprocess.run(docker_command, shell=True, check=True)
	except subprocess.CalledProcessError as docker_error:
    		print(f"Error running Docker command: {docker_error}")
		
	for idx,i in enumerate(file_paths):
		update_progress_bar(idx + 1, len(file_paths))
		os.system('sudo docker cp '+str(i)+'/'+os.path.basename(str(i))+'.nii.gz vertebral_labeling:/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/'+os.path.basename(str(i))+'_0000.nii.gz')
		os.system('sudo docker start vertebral_labeling')
		comando_1 = 'sudo docker exec -it vertebral_labeling python3 /home/scripts/cuda.py'
		comando_2 = 'sudo docker exec -it vertebral_labeling python3 /home/scripts/cpu.py'
		container_name = 'vertebral_labeling'
		command_1 = 'sudo docker exec -it vertebral_labeling python3 /home/scripts/cuda.py'
		file_to_check = '/home/datav2/inference/761_SCT/preds/'+os.path.basename(str(i))+'.nii.gz'
		command_2 = 'sudo docker exec -it vertebral_labeling python3 /home/scripts/cpu.py'		
		try:
        		subprocess.check_call(comando_1, shell=True, stderr=subprocess.DEVNULL)	
		except subprocess.CalledProcessError as e:
			pass       				
		check_file_command = f'sudo docker exec -it {container_name} test -f {file_to_check} && echo "found" || echo "not found"'
		check_result = subprocess.run(check_file_command, shell=True, stdout=subprocess.PIPE, text=True)
		if "not found" in check_result.stdout:
			print("\033[93mTried to predict on GPU, but your GPU is not able to work on this task. Please check your CUDA settings\033[0m")
			print('\033[95m\033[1mNow trying to perform on CPU, this may take much more time to finish\033[0m')
			subprocess.run(command_2, shell=True)			
		os.system('sudo docker exec -it vertebral_labeling chmod -R 777 /home/datav2/inference/761_SCT/preds/'+os.path.basename(str(i))+'.nii.gz')
		os.system('sudo docker cp vertebral_labeling:/home/datav2/inference/761_SCT/preds/'+os.path.basename(str(i))+'.nii.gz'+' '+str(i)+'/'+os.path.basename(str(i))+'_seg_labeled.nii.gz')
		os.system('sudo docker exec -it vertebral_labeling rm -f /home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/'+os.path.basename(str(i))+'_0000.nii.gz')
		os.system('cd '+str(i)+' && sct_qc -i '+os.path.basename(str(i))+'.nii.gz -s '+os.path.basename(str(i))+'_seg_labeled.nii.gz'+' -p sct_label_vertebrae')
		os.system('mv -v '+str(i)+'/qc '+str(i)+'/qc_labeled_'+os.path.basename(str(i)))
	os.system('sudo docker stop vertebral_labeling')
	os.system('sudo docker rm vertebral_labeling')
	progress_label.config(text="AUTOMATED LABELING FINISHED!")
	progress_window.update()
	progress_window.after(4000, progress_window.destroy)
	print('\033[92m\033[1mAUTOMATED VERTEBRAL LABELING FINISHED!\033[0m')
	pass	
	
#############################		

def singularity():
	print('\033[94m\033[1mPLEASE SELECT THE PATH OF THE\033[0m \033[92m\033[1menigma2\033[0m \033[94m\033[1mFOLDER\033[0m')
	enigma_folder = tkfilebrowser.askopendirname()
	print('The \033[92m\033[1menigma2\033[0m folder selected is located at: '+enigma_folder)
	print('\033[94m\033[1mNOW SELECT THE WANTED FOLDERS FROM THE\033[0m \033[92m\033[1mspine\033[0m \033[94m\033[1mFOLDER:\033[0m')
	file_paths = tkfilebrowser.askopendirnames()
	
	if not file_paths:
		print('\033[91m\033[1mNo folders selected.\033[0m')
		return
		
	print ('\033[92m\033[1mSelected folders:\033[0m')
	for file_path in file_paths:
		print(file_path)
		
	progress_window = tk.Toplevel()
	progress_window.title("Automated Labeling Progress")

	progress_label = tk.Label(progress_window, text="Labeling...")
	progress_label.pack()

	progress_bar = ttk.Progressbar(progress_window, length=300, mode="determinate")
	progress_bar.pack()

	progress_text = tk.Label(progress_window, text="")
	progress_text.pack()
	
	def update_progress_bar(current, total):
		progress_percent = int((current / total) * 99)
		progress_bar["value"] = progress_percent
		progress_text["text"] = f"{progress_percent}% done"
		progress_window.update()	
		
	for idx,i in enumerate(file_paths):
		os.system('sudo rm vertebral_labeling.simg/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/*nii.gz')
		update_progress_bar(idx + 1, len(file_paths))
		os.system('sudo cp '+str(i)+'/'+os.path.basename(str(i))+'.nii.gz '+enigma_folder)
		os.system('sudo chmod -R 777 '+enigma_folder+'/'+os.path.basename(str(i))+'.nii.gz')
		os.system('sudo mv '+os.path.basename(str(i))+'.nii.gz '+'vertebral_labeling.simg/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/'+os.path.basename(str(i))+'_0000.nii.gz')
		os.system('sudo chmod -R 777 vertebral_labeling.simg/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/'+os.path.basename(str(i))+'_0000.nii.gz')
		command_1 = 'sudo singularity exec --writable --nv vertebral_labeling.simg/ python3 /home/scripts/cuda.py'
		command_2 = 'sudo singularity exec --writable --nv vertebral_labeling.simg/ python3 /home/scripts/cpu.py'
		try:
        		subprocess.check_call(command_1, shell=True, stderr=subprocess.DEVNULL)	
		except subprocess.CalledProcessError as e:
			pass  
		dire = 'vertebral_labeling.simg/home/datav2/inference/761_SCT/preds/'
		file1 = os.path.basename(str(i))+'.nii.gz'
		way = os.path.join(dire, file1)	     				
		if os.path.exists(way):
			print('OK')
		else:	
			print("\033[93mTried to predict on GPU, but your GPU is not able to work on this task. Please check your CUDA settings\033[0m")
			print('\033[95m\033[1mNow trying to perform on CPU, this may take much more time to finish\033[0m')
			subprocess.run(command_2, shell=True)
		os.system('sudo chmod -R 777 vertebral_labeling.simg/home/datav2/inference/761_SCT/preds/'+os.path.basename(str(i))+'.nii.gz')
		os.system('mv -v '+enigma_folder+'/vertebral_labeling.simg/home/datav2/inference/761_SCT/preds/'+os.path.basename(str(i))+'.nii.gz '+enigma_folder+'/vertebral_labeling.simg/home/datav2/inference/761_SCT/preds/'+os.path.basename(str(i))+'_seg_labeled.nii.gz')
		os.system('sudo rm vertebral_labeling.simg/home/datav2/nnUNet_raw/Dataset761_SCT/imagesTs/*nii.gz')
		os.system('sudo mv '+enigma_folder+'/'+'vertebral_labeling.simg/home/datav2/inference/761_SCT/preds/'+os.path.basename(str(i))+'_seg_labeled.nii.gz '+enigma_folder)
		os.system('sudo mv '+enigma_folder+'/'+os.path.basename(str(i))+'_seg_labeled.nii.gz '+str(i))
		os.system('sudo rm '+enigma_folder+'/'+os.path.basename(str(i))+'.nii.gz')
		os.system('cd '+str(i)+' && sct_qc -i '+os.path.basename(str(i))+'.nii.gz -s '+os.path.basename(str(i))+'_seg_labeled.nii.gz'+' -p sct_label_vertebrae')
		os.system('sudo mv -v '+str(i)+'/qc '+str(i)+'/qc_labeled_'+os.path.basename(str(i)))
	progress_label.config(text="AUTOMATED LABELING FINISHED!")
	progress_window.update()
	progress_window.after(4000, progress_window.destroy)
	print('\033[92m\033[1mAUTOMATED VERTEBRAL LABELING FINISHED!\033[0m')
	pass	
			
															
#############################  

def reg_aut():
	file_paths = tkfilebrowser.askopendirnames()
	
	if not file_paths:
		print('\033[91m\033[1mNo folders selected.\033[0m')
		return
		
	print ('\033[92m\033[1mSelected folders:\033[0m')
	for file_path in file_paths:
		print(file_path)
		
	progress_window = tk.Toplevel()
	progress_window.title("Automated Registration Progress")

	progress_label = tk.Label(progress_window, text="Registering...")
	progress_label.pack()

	progress_bar = ttk.Progressbar(progress_window, length=300, mode="determinate")
	progress_bar.pack()

	progress_text = tk.Label(progress_window, text="")
	progress_text.pack()
	
	def update_progress_bar(current, total):
		progress_percent = int((current / total) * 99)
		progress_bar["value"] = progress_percent
		progress_text["text"] = f"{progress_percent}% done"
		progress_window.update()	
		
	for idx, i in enumerate(file_paths):
		update_progress_bar(idx + 1, len(file_paths))
		os.system('cd '+str(i)+' && sct_label_utils -i '+os.path.basename(str(i))+'_seg_labeled.nii.gz'+' -vert-body 2,3 -o '+os.path.basename(str(i))+'_labels_vert.nii.gz')
		os.system('cd '+str(i)+' && sct_register_to_template -i '+os.path.basename(str(i))+'.nii.gz'+' -s '+os.path.basename(str(i))+'_seg.nii.gz -l '+os.path.basename(str(i))+'_labels_vert.nii.gz -c t1 -qc qc_'+os.path.basename(str(i)))
		os.system('cd '+str(i)+' && sct_warp_template -d '+os.path.basename(str(i))+'.nii.gz -w warp_template2anat.nii.gz -qc qc_'+os.path.basename(str(i)))
	progress_label.config(text="AUTOMATED REGISTRATION FINISHED!")
	progress_window.update()
	progress_window.after(4000, progress_window.destroy)	
	print ('\033[92m\033[1mAUTOMATED SPINAL CORD REGISTRATION FINISHED!\033[0m')    

#############################

def manual():
	file_paths = tkfilebrowser.askopendirnames()
	
	if not file_paths:
		print('\033[91m\033[1mNo folders selected.\033[0m')
		return
		
	print ('\033[92m\033[1mSelected folders:\033[0m')
	for file_path in file_paths:
		print(file_path)
		
	progress_window = tk.Toplevel()
	progress_window.title("Manual Registration Progress")

	progress_label = tk.Label(progress_window, text="Registering...")
	progress_label.pack()

	progress_bar = ttk.Progressbar(progress_window, length=300, mode="determinate")
	progress_bar.pack()

	progress_text = tk.Label(progress_window, text="")
	progress_text.pack()
	
	def update_progress_bar(current, total):
		progress_percent = int((current / total) * 99)
		progress_bar["value"] = progress_percent
		progress_text["text"] = f"{progress_percent}% done"
		progress_window.update()	
		
	for idx, i in enumerate(file_paths):
		update_progress_bar(idx + 1, len(file_paths))
		os.system('cd '+str(i)+' && sct_label_utils -i '+os.path.basename(str(i))+'.nii.gz'+' -create-viewer 2,3 -o '+os.path.basename(str(i))+'_labels_disc.nii.gz')
	progress_label.config(text="Packing Done!")
	progress_window.update()
	progress_window.after(4000, progress_window.destroy)	
	print ('\033[92m\033[1mMANUAL VERTEBRAL LABELING FINISHED!\033[0m') 	

#############################

def reg_man():
	file_paths = tkfilebrowser.askopendirnames()
	
	if not file_paths:
		print('\033[91m\033[1mNo folders selected.\033[0m')
		return
		
	print ('\033[92m\033[1mSelected folders:\033[0m')
	for file_path in file_paths:
		print(file_path)
		
	progress_window = tk.Toplevel()
	progress_window.title("Manual Registration Progress")

	progress_label = tk.Label(progress_window, text="Registering...")
	progress_label.pack()

	progress_bar = ttk.Progressbar(progress_window, length=300, mode="determinate")
	progress_bar.pack()

	progress_text = tk.Label(progress_window, text="")
	progress_text.pack()
	
	def update_progress_bar(current, total):
		progress_percent = int((current / total) * 99)
		progress_bar["value"] = progress_percent
		progress_text["text"] = f"{progress_percent}% done"
		progress_window.update()	
		
	for idx, i in enumerate(file_paths):
		update_progress_bar(idx + 1, len(file_paths))
		os.system('cd '+str(i)+' && sct_register_to_template -i '+os.path.basename(str(i))+'.nii.gz'+' -s '+os.path.basename(str(i))+'_seg.nii.gz -ldisc '+os.path.basename(str(i))+'_labels_disc.nii.gz -c t1 -qc qc_'+os.path.basename(str(i)))
	progress_label.config(text="Packing Done!")
	progress_window.update()
	progress_window.after(4000, progress_window.destroy)	
	print ('\033[92m\033[1mMANUAL SPINAL CORD REGISTRATION FINISHED!\033[0m')	
		
#############################

def ext():
	file_paths = tkfilebrowser.askopendirnames()
	
	data = ["subject", "CSA C1", "CSA C2", "CSA C3"]
	data2 = ["subject", "Mean(eccentricity) C1", "Mean(eccentricity) C2", "Mean(eccentricity) C3"]
	now = datetime.now()
	hour = str(now.strftime("%m-%d-%Y_%H-%M-%S"))
	before = str(file_paths[0])
	before = os.path.dirname(before)
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
	
	if not file_paths:
		print('\033[91m\033[1mNo folders selected.\033[0m')
		return
		
	print ('\033[92m\033[1mSelected folders:\033[0m')
	for file_path in file_paths:
		print(file_path)
		
	progress_window = tk.Toplevel()
	progress_window.title("Data Extraction Progress")

	progress_label = tk.Label(progress_window, text="Extracting...")
	progress_label.pack()

	progress_bar = ttk.Progressbar(progress_window, length=300, mode="determinate")
	progress_bar.pack()

	progress_text = tk.Label(progress_window, text="")
	progress_text.pack()
	
	def update_progress_bar(current, total):
		progress_percent = int((current / total) * 99)
		progress_bar["value"] = progress_percent
		progress_text["text"] = f"{progress_percent}% done"
		progress_window.update()	
	
	for idx,i in enumerate(file_paths):
		v = []
		k = []
		b1 = []
		update_progress_bar(idx + 1, len(file_paths))
		os.system('cd '+str(i)+' && sct_process_segmentation -i '+os.path.basename(str(i))+'_seg.nii.gz -vert 1:3 -perlevel 1 -o '+os.path.basename(str(i))+'_csa.csv')
		with open(str(i)+'/'+os.path.basename(str(i))+'_csa.csv', 'r', encoding='utf-8') as file:
			sp = csv.reader(file)
			for row in sp:
				v.append(row)		
		k.append(os.path.basename(str(i)))
		b1.append(os.path.basename(str(i)))		
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
										
	progress_label.config(text="Packing Done!")
	progress_window.update()
	progress_window.after(4000, progress_window.destroy)	
	print ('\033[92m\033[1mDATA EXTRACTION FINISHED!\033[0m')	
	
		
#############################	

def pack():
	file_paths = tkfilebrowser.askopendirnames()
	
	if not file_paths:
		print('\033[91m\033[1mNo folders selected.\033[0m')
		return
		
	print ('\033[92m\033[1mSelected folders:\033[0m')
	for file_path in file_paths:
		print(file_path)
		
	before = str(file_paths[0])
	before = os.path.dirname(before)
	
	progress_window = tk.Toplevel()
	progress_window.title("Packing Progress")

	progress_label = tk.Label(progress_window, text="Packing...")
	progress_label.pack()

	progress_bar = ttk.Progressbar(progress_window, length=300, mode="determinate")
	progress_bar.pack()

	progress_text = tk.Label(progress_window, text="")
	progress_text.pack()
	
	def update_progress_bar(current, total):
		progress_percent = int((current / total) * 99)
		progress_bar["value"] = progress_percent
		progress_text["text"] = f"{progress_percent}% done"
		progress_window.update()	
	
	for idx, i in enumerate(file_paths):
		update_progress_bar(idx + 1, len(file_paths))
		os.system('cd '+str(before)+' && zip -r '+os.path.basename(str(i))+'.zip'+' '+os.path.basename(str(i))+' -x '+os.path.basename(str(i))+'/'+os.path.basename(str(i))+'.nii.gz')
	progress_label.config(text="Packing Done!")
	progress_window.update()
	progress_window.after(4000, progress_window.destroy)	
	print ('\033[92m\033[1mDATA PACKED AND READY TO GO!\033[0m')
	print ('\033[94m\033[1mZIP files located at: '+str(before)+'\033[0m')		
			
#############################

def open_checkbox_window():
    checkbox_window = tk.Toplevel(root)
    checkbox_window.title("Choose Platform")

    def on_checkbox_click():
        choice = "Docker" if container_choice.get() == "Docker" else "Singularity"
        checkbox_window.destroy()
        automated(choice)

    container_choice = tk.StringVar()

    checkbox_frame = tk.Frame(checkbox_window)
    checkbox_frame.pack(side="top", pady=(10, 0))

    docker_button = tk.Radiobutton(checkbox_frame, text="Docker", variable=container_choice, value="Docker")
    docker_button.pack(side="left", padx=(0, 10))

    singularity_button = tk.Radiobutton(checkbox_frame, text="Singularity", variable=container_choice, value="Singularity")
    singularity_button.pack(side="left")

    ok_button = tk.Button(checkbox_window, text="OK", command=on_checkbox_click)
    ok_button.pack(side="top", pady=(10, 0))

    button_x, button_y, _, _ = ok_button.bbox("insert")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_position = root.winfo_x() + button_x
    y_position = root.winfo_y() + button_y

    checkbox_window.geometry(f"250x100+{x_position}+{y_position}")

def automated(choice):
    if choice:
        if choice == "Docker":
            docker()
            print("Running on Docker...")
        elif choice == "Singularity":
            singularity()
            print("Running on Singularity...")
            
#############################

def open_tutorial():
    url = "https://github.com/art2mri/enigma2" 
    webbrowser.open_new(url)
    
#############################	

root = tk.Tk()
root.title("enigma2")

window_width = 520
window_height = 860
root.geometry(f"{window_width}x{window_height}")
root.configure(bg='gray')

image_path = "files/gj.png"  
img = Image.open(image_path)

img = img.resize((250, 250))

img = ImageTk.PhotoImage(img)

title_label = tk.Label(root, text="Spinal Cord Segmentation", bg='gray', font=("Helvetica", 20, "bold"))
title_label.pack(pady=10)

subtitle_label = tk.Label(root, text="Spinal Cord Toolbox", bg='gray', font=("Helvetica", 16))
subtitle_label.pack(pady=5)

image_label = tk.Label(root, image=img, bg='gray')
image_label.pack()

images_path_button = tk.Button(root, text="Prepare Folders", height=2, width=20, command=browse_folder, highlightbackground="black", highlightthickness=2)
spinal_cord_segmentation_button = tk.Button(root, text="Spinal Cord Segmentation", height=2, width=20, command=modal_1, highlightbackground="black", highlightthickness=2)
label_text = tk.Label(root, text="Spinal Cord Vertebral Labeling", bg='gray', font=("Helvetica", 15, "bold"))

images_path_button.pack(pady=10)
spinal_cord_segmentation_button.pack(pady=10)
label_text.pack(pady=10)

button_frame = tk.Frame(root, bg='gray')
button_frame.pack(pady=10)

automated_frame = tk.Frame(button_frame, bg='darkgray', padx=4, pady=4, highlightbackground="black", highlightthickness=2)
automated_frame.grid(row=0, column=0, padx=(10, 22), pady=(10,10))

container_choice = tk.StringVar()
container_choice.set("")

automated_button = tk.Button(automated_frame, text="Automated", height=2, width=17, command=open_checkbox_window, highlightbackground="black", highlightthickness=2)
automated_button.pack(fill='both', expand=True, pady=(0, 5))

manual_frame = tk.Frame(button_frame, bg='darkgray', padx=4, pady=4, highlightbackground="black", highlightthickness=2)
manual_frame.grid(row=0, column=1, padx=(22, 10), pady=(10,10))

manual_button = tk.Button(manual_frame, text="Manual", height=2, width=17,command=manual, highlightbackground="black", highlightthickness=2)
manual_button.pack(fill='both', expand=True, pady=(0, 5))

spinal_cord_registration_automated = tk.Button(automated_frame, text="Spinal Cord Registration", height=2, width=17, command=reg_aut, highlightbackground="black", highlightthickness=2)
spinal_cord_registration_automated.pack(fill='both', expand=True)

spinal_cord_registration_manual = tk.Button(manual_frame, text="Spinal Cord Registration", height=2, width=17, command=reg_man, highlightbackground="black", highlightthickness=2)
spinal_cord_registration_manual.pack(fill='both', expand=True)

additional_button_frame = tk.Frame(root, bg='gray')
additional_button_frame.pack(pady=10)

data_extraction = tk.Button(additional_button_frame, text="Data Extraction", height=2, width=20, command=ext, highlightbackground="black", highlightthickness=2)
send_button = tk.Button(additional_button_frame, text="Pack and Send", height=2, width=20, command=pack, highlightbackground="black", highlightthickness=2)

data_extraction.pack(pady=(10, 10))
send_button.pack(pady=(10, 10))

version_label = tk.Label(root, text="Version 2.0", bg='gray', font=("Helvetica", 11, "bold"))
version_label.place(relx=1.0, rely=1.0, anchor='se', bordermode='outside', x=-10, y=-10)

tutorial_button = tk.Button(root, text="Tutorial", height=1, width=5, highlightbackground="black", highlightthickness=2, command=open_tutorial)
tutorial_button.place(relx=0.0, rely=1.0, anchor='sw', bordermode='outside', x=10, y=-10)

button_frame.grid_columnconfigure(0, weight=1)
additional_button_frame.grid_columnconfigure(0, weight=1)

root.mainloop()
