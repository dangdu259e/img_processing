import numpy as np
import cv2

# in bellow codeline, have to change path to where image belong to
image = cv2.imread('../../image/7.png')

cv2.imshow("Test Image", image)

# image.shape
(height, width, dim) = image.shape
print("height: ", height)
print("width: ", width)
print("channels: ", dim)  # hiển thị số kênh màu của ảnh

print(max(max((image[:, :, 1]), key=max)))

k = cv2.waitKey(0)  # output is ASCII(character)

if k == 27:  # wait for esc key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save to a grey image and exit
    if dim == 1:  # case that original image is grayscale ready
        cv2.imwrite("./save_ouput/7Gray.jpg", image)

    else:  # case that original image is colour

        # method 1: use standard lib OpenCV to convert: cv2.cvtColor()
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # kích thước của ảnh mới
        print("Shape new image: ", gray_image.shape)
        # write to jpg
        cv2.imwrite("../save_ouput/7Gray_standard.jpg", gray_image)

        # method 2: calculate by formular
        gray_img2 = image[:, :, 2] * 0.2989 + image[:, :, 1] * 0.5870 + image[:, :, 0] * 0.1140
        print(gray_img2.shape)
        cv2.imwrite("../save_ouput/7Gray_formular.jpg", gray_img2)

    cv2.destroyAllWindows()
