#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
from matplotlib import pyplot as plt


# In[2]:


# Bai tap 02 hw01


# In[3]:


# read image
# read image low_contract.jpg
image = cv2.imread('../image/low_contract.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image)
plt.title('original image')


# In[4]:


# Convert RGB to HSV
img_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
plt.imshow(img_hsv)
plt.title("HSV image")


# 2.a. Tăng độ bão hòa màu lên bằng 150% so với ảnh gốc, ghi ảnh kết quả vào low_contract_edit1.png

# In[5]:


# increase the SATURATION to 150% (1.50)
img_hsv_2a = img_hsv
img_hsv_2a [:, :, 1]= img_hsv_2a [:, :, 1]*1.50

# reconvert hsv to rgb
img_hsv_2a = cv2.cvtColor(img_hsv_2a, cv2.COLOR_HSV2RGB)
plt.imshow(img_hsv_2a)
plt.title("SATURATION 150%")

# write result to low_contract_edit1.png
cv2.imwrite('./save_output/low_contract_edit1.png', img_hsv_2a)


# 2.b. Giảm độ sáng xuống còn 75% so với ảnh gốc, ghi ảnh kết quả vào low_contract_edit2.png

# In[6]:


# decrease the SATURATION to 75% (0.75)
img_hsv_2b = img_hsv
img_hsv_2b [:, :, 1]= img_hsv_2b [:, :, 1]*0.75

# reconvert hsv to rgb
img_hsv_2b = cv2.cvtColor(img_hsv_2b, cv2.COLOR_HSV2RGB)
plt.imshow(img_hsv_2b)
plt.title("SATURATION 75%")

# write result to low_contract_edit2.png
cv2.imwrite('./save_output/low_contract_edit2.png', img_hsv_2b)

