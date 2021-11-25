import cv2
import numpy as np
from matplotlib import pyplot as plt

img = np.array([[1, 2, 3, 4, 5, 6],
                  [0, 1, 7, 3, 4, 5],
                  [0, 0, 1, 2, 3, 4],
                  [0, 12, 0, 1, 2, 3],
                  [0, 266, 0, 0, 1, 2]]
                 )



# read image
# in bellow codeline, have to change path to where image belong to
image = cv2.imread('../../tuan01/image/7.png')
cv2.imshow("Test Image", image)

print(image)
print(type(image))
img_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
tmp = img_hsv[:, :, 1]
tmp = tmp * 125
tmp[tmp > 255] = 255
print(tmp)