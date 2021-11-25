#!/usr/bin/env python
# coding: utf-8

# bài 3_ hw01. Viết đoạn mã lệnh (python) kiểm tra xem histogram một ảnh có bị dồn tập trung vào khoảng nào hay không
# (tức là các điểm ảnh chỉ có giá trị cường độ xám trong một khoảng, phía ngoài khoảng đó không có điểm nào).

# In[16]:


import numpy as np
import cv2
from matplotlib import pyplot as plt


# In[17]:


# read image
image = cv2.imread('../image/8.png')

# show image 
cv2.imshow("Test Image", image)
k = cv2.waitKey(0)  # output is ASCII(character)


# In[18]:


# convert BGR to GRAY
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey Image", gray_image)
k = cv2.waitKey(0)  # output is ASCII(character)


# In[19]:


# create histogram 
histogram, bin_edges = np.histogram(image,bins = 256, range=(0, 255))


# In[20]:


# configure and draw the histogram figure
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Grayscale value")
plt.ylabel("pixel")

plt.xlim([0.0, 255.0]) #for 255 levels of gray scale
plt.plot(bin_edges[0:-1], histogram) # plot histogram

plt.show()

