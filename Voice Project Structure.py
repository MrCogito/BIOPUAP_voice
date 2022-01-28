#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import math
import librosa
import time
import numpy as np
import shutil


# In[3]:


DATASET_PATH = "D:/DownloadsD/DS_10283_3443/VCTK-Corpus-0.92"
#DATASET_PATH = "D:/DownloadsD/tatoeba_audio_eng"
#DATASET_PATH = "D:/DownloadsD/dev-clean/"


# In[4]:


def create_new_folder(newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)

def move_file(source_path, target_path):
        file_names = os.listdir(source_path)

        for file_name in file_names:
            if file_name != target_path:
                shutil.move(os.path.join(source_path, file_name), target_path)

def get_folders(dir_path):
    return [ name for name in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, name)) ]
    
                
def speaker_folders(folder_path):
    file_list_ = os.listdir(folder_path)
    for file in file_list_:
            speaker_path = os.path.join(folder_path, file)
            if os.path.isdir(speaker_path):
                subfolder_list = get_folders(speaker_path)
                #speaker_files = os.listdir(speaker_path)
                #temp_path = os.path.join(speaker_path, file)
                #condition = os.path.isdir(temp_path)
                #subfolder_list = [folder for folder in speaker_files if condition]
                # jezeli jest pusta
                if len(subfolder_list) == 0:
                    new_subfolder_path = os.path.join(speaker_path, 'subfolder')
                    create_new_folder(new_subfolder_path)
                    move_file(speaker_path,new_subfolder_path)
                    


# In[5]:


def folder_structure_parser(DATASET_PATH):
    file_list = os.listdir(DATASET_PATH)
    print(file_list)
    for file in file_list:
        file_path = os.path.join(DATASET_PATH,file)
        if os.path.isdir(file_path):
            print(file_path)
            file_list_2 = os.listdir(file_path)
            no_of_files = len(file_list_2)
            print(file_list_2)
            if no_of_files > 7:
                new_folder_path = os.path.join(file_path, 'temp')
                create_new_folder(new_folder_path)
                move_file(file_path,new_folder_path)
                
                file_list_ = os.listdir(new_folder_path)
                speaker_folders(file_list_,new_folder_path)
            
            else:
                folders = get_folders(file_path)
                print(folders)
                for folder in folders:
                    folder_path = os.path.join(file_path, folder)
                    speaker_folders(folder_path)
                            
                
    


# In[6]:


folder_structure_parser(DATASET_PATH)


# In[ ]:


# co sie udalo, udalo sie zmienic strukture VCTK Corpus i tatoeba_audio i ma tyle samo poziomow co librispeech

