import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('../../image/13.jpg')

# convert image (above) to gray scale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# create Histogram
histogram, bin_edges = np.histogram(image, bins=256, range=(0, 255))

# configure and draw the histogram figure
plot1 = plt.figure(1)
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim([0.0, 255.0])  # for 255 levels of gray scale

plt.plot(bin_edges[0:-1], histogram)  # <- plot histogram
plt.show()

# Vẽ biểu đồ histogram cho từng kênh màu
# tuple to select colors of each channel line
colors = ('red', 'green', 'blue')
channel_ids = (0, 1, 2)

# create the histogram plot, with 3 line, one for each color
plot2 = plt.figure(2)
plt.xlim([0, 256])
for channel_ids, c in zip(channel_ids, colors):
    histogram, bin_edges = np.histogram(
        image[:, :, channel_ids], bins=256, range=(0, 255)
    )
    plt.plot(bin_edges[0: -1], histogram, color=c)

plt.xlabel("Color value")
plt.ylabel("Pixels")
plt.show()
