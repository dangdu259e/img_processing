import cv2
import numpy as np
import os


# open (Erosion-> Dilation)
def img_erosion_dilation(kernel, path, filename):
    # Taking a matrix of size 5 as the kernel
    img = cv2.imread(path, 0)
    img_erosion = cv2.erode(img, kernel, iterations=1)
    img_dilation = cv2.dilate(img_erosion, kernel, iterations=1)

    # save result image
    output_open_Erosion_Dilation = 'output_open_Erosion_Dilation/' + filename
    cv2.imwrite(output_open_Erosion_Dilation, img_dilation)

    cv2.imshow('Input', img)
    cv2.imshow('output_open_Erosion_Dilation', img_dilation)

    k = cv2.waitKey(0)
    if k == 27:  # wait for ESC key to exit
        cv2.destroyAllWindows()


# close (Dilation -> Erosion)
def img_dilation_erosion(kernel, path, filename):
    # Taking a matrix of size 5 as the kernel
    img = cv2.imread(path, 0)

    img_dilation = cv2.dilate(img, kernel, iterations=1)
    img_erosion = cv2.erode(img_dilation, kernel, iterations=1)

    # save result image
    output_close_Dilation_Erosion = 'output_close_Dilation_Erosion/' + filename
    cv2.imwrite(output_close_Dilation_Erosion, img_erosion)

    cv2.imshow('Input', img)
    cv2.imshow('output_close_Dilation_Erosion', img_erosion)

    k = cv2.waitKey(0)
    if k == 27:  # wait for ESC key to exit
        cv2.destroyAllWindows()


if __name__ == '__main__':
    folder = "../img"
    # all file image
    images = os.listdir(folder)
    kernel = np.ones((5, 5), np.uint8)
    # Reading the input image
    img = cv2.imread('', 0)
    for i in range(0, len(images)):
        images_path = folder + "/" + images[i]
        img_open = img_erosion_dilation(kernel=kernel, path=images_path, filename=images[i])
        img_close = img_dilation_erosion(kernel=kernel, path=images_path, filename=images[i])
