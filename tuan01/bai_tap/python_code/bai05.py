#!/usr/bin/env python
# coding: utf-8

# In[17]:


# bai05:hw1 cân bằng histogram


# In[18]:


import numpy as np
import cv2
from matplotlib import pyplot as plt


# In[30]:


# ảnh thử nghiệm
images = ['low_contract.jpg', '7_1.png', 'contrast.jpg', 'too_bright.png', '7.png', '8.png', '13.jpg']

import os
# folder image
cwd = os.getcwd()
os.chdir('../image/')
print(cwd)

fig, axs = plt.subplots(nrows=7, ncols=2, figsize=(30, 30))


# image test
for i, name in enumerate(images):
    image = cv2.imread(os.path.join(cwd, name))
    
    # convert image from RGB to HSV
    img_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    # Histogram equalisation on the V-channel
    img_hsv[:, :, 2] = cv2.equalizeHist(img_hsv[:, :, 2])

    # convert image back from HSV to RGB
    image_new = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)
    
    axs[i][0].imshow(image[:,:,::-1])
    axs[i][0].set_title("Origin")
    
    axs[i][1].imshow(image_new[:,:,::-1])
    axs[i][1].set_title("New Image")

