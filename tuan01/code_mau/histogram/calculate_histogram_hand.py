import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('../../image/13.jpg')
# convert image (above) to gray scale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Đoạn lệnh sau tính Histogram của ảnh Gray scale không sử dụng thư viện
histgrm = np.zeros(256, np.int32)
for i in range(0, gray_image.shape[0]):
    for j in range(0, gray_image.shape[1]):
        histgrm[gray_image[i][j]] += 1
# now histogram is in bins already
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixels")
plt.xlim([0, 255])  # for 255 levels of gray scale
plt.plot(histgrm)
plt.show()
