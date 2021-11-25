import cv2

image = cv2.imread('../../image/13.jpg')
c = 20  # chang value of c as you need
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Image: ',gray_image)
gray_image += c

# check that pixels value > max = 255
gray_image[gray_image > 255] = 255

# check that pixels value < min = 0
gray_image[gray_image < 0] = 0

cv2.imshow("change gray values", gray_image)

k = cv2.waitKey(0)
if (k == 27):  # wait for ESC key to exit
    cv2.destroyAllWindows()
