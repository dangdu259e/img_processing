import cv2

# read image
# in bellow codeline, have to change path to where image belong to
image = cv2.imread('../../image/7.png')
cv2.imshow("Test Image", image)

# BGR to HSV
img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("Image HSV color", img_hsv)

# decrease the SATURATION to 75% (0.75)
# note that SATURATION is from 0 to 255 (not [0, 1])
img_hsv[:, :, 1] = img_hsv[:, :, 1] * 0.75
cv2.imshow("Image HSV_SATURATION color", img_hsv)

# reconvert from HSV back to RGB
img_rgb1 = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("Image RGB color", img_rgb1)

#show new image
cv2.imshow("Decrease SATURATION image: ", img_rgb1)
k = cv2.waitKey(0)
if(k == 27):
    cv2.destroyAllWindows()

cv2.imwrite('../save_ouput/7_DEC_SATURATION.png', img_rgb1)


