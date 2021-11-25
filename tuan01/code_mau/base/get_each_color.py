import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('../../image/8.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

fig = plt.figure()
columns = 3
rows = 1

# Lấy ra từng màu
red_channels = np.zeros(image.shape, dtype='uint8')
red_channels[:, :, 0] = image[:, :, 0]
fig.add_subplot(rows, columns, 1)
plt.title("red_channels")
plt.imshow(red_channels)


green_channels = np.zeros(image.shape, dtype='uint8')
green_channels[:, :, 1] = image[:, :, 1]
fig.add_subplot(rows, columns,2)
plt.title("green_channels")
plt.imshow(green_channels)

blue_channels = np.zeros(image.shape, dtype='uint8')
blue_channels[:, :, 2] = image[:, :, 2]
fig.add_subplot(rows, columns,3)
plt.title("blue_channels")
plt.imshow(blue_channels)
plt.subplots_adjust(right=1.5)   # khoảng cách giữa các ảnh
plt.show()
