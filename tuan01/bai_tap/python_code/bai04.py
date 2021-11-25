#!/usr/bin/env python
# coding: utf-8

#     4.Nếu có, hãy dùng các phương pháp sau để tăng/giảm độ tương phản:
#     4.a. Nếu cường độ tập trung vào vùng thấp (ảnh tối) hoặc vùng cao (ảnh sáng):
#     hãy dùng biến đổi gamma với các giá trị gamma tương ứng (nhỏ hoặc lớn) để điều chỉnh độ tương phản
#     (các bạn cần tự phát hiện ảnh tập trung ở cường độ sáng cao hay thấp).
# 
#     4.b. Nếu cường độ tập trung vào vùng giữa, hãy dùng biến đổi tuyến tính từng khúc để điều chỉnh histogram.
# 
#     Thử với các ảnh low_contract.jpg, 7_1.png, contrast.jpg, too_bright.png và lưu ảnh kết quả với tên file khác nhau.

# In[110]:


import numpy as np
import cv2
from matplotlib import pyplot as plt


# In[111]:


# read image
image = cv2.imread('../image/low_contract.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# show image
plt.subplot(1,2,1)
plt.title("Original image")
plt.imshow(image)

# convert BGR to GRAY
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
plt.subplot(1,2,2)
plt.title("Gray image")
plt.imshow(gray_image, cmap='gray')

# create histogram 
histogram, bin_edges = np.histogram(gray_image,bins = 256, range=(0, 255))

# configure and draw the histogram figure
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Grayscale value")
plt.ylabel("pixel")

plt.xlim([0.0, 255.0]) #for 255 levels of gray scale
plt.plot(bin_edges[0:-1], histogram) # plot histogram

plt.show()


# In[112]:


#dựa vào histogram ==> bức ảnh có mức sáng rất cao => bức ảnh low_contract.jpg => cần thực hiện cho contract lên cao


# In[113]:


# 4a) Thực hiện biến đổi gamma tập trung vào vùng ảnh
# gamma function
def adjust_image_gamma(image, gamma = 1.0):
    image_new = np.power(image, gamma) # compute I^gamma
    max_val = np.max(image_new.ravel()) # compute max value of new image
    c = 255/ max_val # compute c, maximum gray level is 255
    image_new = image_new * c # G = c.I^gamma
    image_new = image_new.astype(np.uint8) # set type to un integer 8 bits
    return image_new


# In[114]:


# low_contract.jpg
low_contract_test = adjust_image_gamma(image, gamma = 0.7)
plt.subplot(1,3,1)
plt.imshow(image)
plt.title("Original image")

plt.subplot(1,3,2)
plt.imshow(low_contract_test)
plt.title("Down contract image")

hight_contract_test = adjust_image_gamma(image, gamma = 1.9)
plt.subplot(1,3,3)
plt.imshow(hight_contract_test)
plt.title("Up contract image")


# Qua đó ta thấy chỉnh hệ số gamma cao lên là bức ảnh trông sẽ rõ nét hơn

# In[115]:


# Những ảnh khác cần kiểm tra 
import os
# folder image
cwd = os.getcwd()
os.chdir('../image/')
print(cwd)

# name_image_test
images = ['low_contract.jpg', '7_1.png', 'contrast.jpg', 'too_bright.png']
fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(30, 30))

# image test
for i, name in enumerate(images):
    image = cv2.imread(os.path.join(cwd, name))
    image_low_gamma = adjust_image_gamma(image, 0.4)
    image_high_gamma = adjust_image_gamma(image, 1.8)
    axs[i][0].imshow(image_low_gamma[:,:,::-1])
    axs[i][0].set_title("Low gamma")
    
    axs[i][1].imshow(image[:,:,::-1])
    axs[i][1].set_title("Origin")
    
    axs[i][2].imshow(image_high_gamma[:,:,::-1])
    axs[i][2].set_title("High gamma")
    


# In[116]:


# 4.b. Nếu cường độ tập trung vào vùng giữa, hãy dùng biến đổi tuyến tính từng khúc để điều chỉnh histogram.

# Find pice-linear transfrom
def Stretch_value(I, a, b, Ga, Gb):
    if (0 <= I and I <= a):
        G = (Ga / a)* I
    elif (a < I and I <= b):
        G = ((Gb - Ga)/(b - a))*(I - a)+ Ga
    else:
        G = ((255 - Gb)/(255 - b))*( I - b)+ Gb
    return G


def Contrast_stretch(image, a, b, Ga, Gb):
    for i in range(image.shape[0]):
        for j in range(image.shape[0]):
            image[i,j] = Stretch_value(image[i,j], a, b, Ga, Gb)
    return image


# default
# a = 100
# b = 230
Ga = 0
Gb = 255

# Những ảnh khác cần kiểm tra 
import os
# folder image
cwd = os.getcwd()
os.chdir('../image/')
print(cwd)

# name_image_test
images = ['low_contract.jpg', '7_1.png', 'contrast.jpg', 'too_bright.png']

fig, axs = plt.subplots(4,figsize=(10,20),squeeze=False)
fig.tight_layout(pad=8.0)

# image test
for i, name in enumerate(images):
    image = cv2.imread(os.path.join(cwd, name))
    
    # convert BGR to GRAY
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    # create histogram 
    histogram, bin_edges = np.histogram(gray_image,bins = 256, range=(0, 255))

    
    # configure and draw the histogram figure
    axs[i][0].set_title(images[i])

    axs[i][0].set_xlim([0.0, 255.0]) #for 255 levels of gray scale
    axs[i][0].plot(bin_edges[0:-1], histogram) # plot histogram


# In[117]:


# # dựa vào đồ thị ta lấy ra các khoảng bị tập trung vùng
# ab = [(100, 250), (200, 225), (0, 50), (200, 250)]
# fig, axs = plt.subplots(nrows=4, ncols=2, figsize=(30, 30))

# for i, name in enumerate(images):
#     image = cv2.imread(os.path.join(cwd, name))
# #     a = ab[i][0]
# #     b = ab[i][1]
#     # convert BGR to GRAY
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     image_new = Contrast_stretch(gray_image, a, b, Ga, Gb)
    
    
#     axs[i][0].imshow(image[:,:,::-1])
#     axs[i][0].set_title("Origin")

#     axs[i][1].imshow(image_new[:,:,::-1])
#     axs[i][1].set_title("Contrast stretch image")

