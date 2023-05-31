#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import tensorflow as tf
import os
import cv2
import matplotlib.pyplot as plt
from tqdm import tqdm

path = "ImagePro"
files=os.listdir(path)

files.sort()

print(files)

image_array=[]
label_array=[]
for i in range(len(files)):
    #list of image in each folder
    sub_file= os.listdir(path+"/"+files[i])
    #print(len(sub_file))
    
    #loop through each subfile
    for j in tqdm(range(len(sub_file))):
        #path of each image
        # Example : Imagepro/A/image_name1.jpg
        file_path=path+"/"+files[i]+"/"+sub_file[j]
        #read each image
        
        image=cv2.imread(file_path)
        
        #resize image by 96x96
        image = cv2.resize(image,(96,96))
        #convert BGR image to RGB image
        
        image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        
        #add this image to image_array
        
        image_array.append(image)
        
        #add label to label array
        # i is number form 0 to len(files)-1
        #so we can use it as label
        label_array.append(i)
        

        
        
        
        
        
        
        
        
        
        
        
        


# In[ ]:




