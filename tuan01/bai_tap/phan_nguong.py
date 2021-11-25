import cv2

img1 = cv2.imread('../image/gamma_corect.png', 0)
img2 = cv2.imread('../image/too_bright.png', 0)
# cv2.imshow('anh', img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Otsu's thresholding
ret1, th1 = cv2.threshold(img1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(ret1)
print(th1)
print('---------------------------')
ret2, th2 = cv2.threshold(img2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print(ret2)
print(th2)
