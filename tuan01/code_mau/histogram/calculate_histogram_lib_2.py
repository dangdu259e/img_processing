import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('../../image/13.jpg')

vals = image.mean(axis=2).flatten()
# plot histogram with 255 bins
b, bins, patches = plt.hist(vals, 255)
plt.xlim([0,255])
plt.show()
