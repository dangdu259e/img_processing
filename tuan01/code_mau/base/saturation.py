import cv2

# read image
# in bellow codeline, have to change path to where image belong to
image = cv2.imread('../../image/7.png')
cv2.imshow("Test Image", image)

img_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
cv2.imshow("HSV color Image", img_hsv)

# decrease the SATURATION to 75% (0.75)
# Note that SATURATION is from 0 to 255 (not[0,1])
img_hsv[:, :, 1] = img_hsv[:, :, 1] * 0.75

# reconvert from HSV back to RGB
img_rgb1 = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)

# show new img
cv2.imshow("Decrease SATURATION image ", img_rgb1)

k = cv2.waitKey(0)

if k == 27:  # wait for esc key to exit
    cv2.destroyAllWindows()
# and then save file DEC. saturation
cv2.imwrite('../save_ouput/7_DEC_SATURATION2.png', img_rgb1)

# increase SATURATION 125%
img_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
tmp = img_hsv[:, :, 1]
tmp = tmp * 125
tmp[tmp > 255] = 255
img_hsv[:, :, 1] = tmp
img_rgb2 = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)
cv2.imshow("test_image", img_rgb2)
k = cv2.waitKey(0)
if k == 27:  # wait for esc key to exit
    cv2.destroyAllWindows()
# and then save file DEC. saturation
cv2.imwrite('../save_ouput/7_DEC_SATURATION2.png', img_rgb1)
