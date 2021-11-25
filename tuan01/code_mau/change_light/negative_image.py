# 6. Lấy âm bản (negative)

import numpy as np
import cv2
from matplotlib import pyplot as plt

# in bellow codeline, have to change path to where image belong to
image = cv2.imread('../../image/gamma_corect.png', 1)
neg_img = 255 - image

cv2.imshow("Negative Image", neg_img)
k = cv2.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()
