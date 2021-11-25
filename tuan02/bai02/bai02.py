# bai02 lam noi duong bien laplacian, sobel
import numpy as np
import cv2
import os

laplacian5 = (1.0 / 16) * np.array([[0, 0, -1, 0, 0],
                                    [0, -1, -2, -1, 0],
                                    [-1, -2, 16, -2, -1],
                                    [0, -1, -2, -1, 0],
                                    [0, 0, -1, 0, 0]])

laplacian3 = (1.0 / 16) * np.array([[0, -1, 0],
                                    [-1, 4, -1],
                                    [0, -1, 0]])
sobelLeft = np.array(([-1, 0, 1],
                      [-2, 0, 2],
                      [-1, 0, 1]))
sobelRight = np.array(([1, 0, -1],
                       [2, 0, -2],
                       [1, 0, -1]))
sobelTop = np.array(([-1, -2, -1],
                     [0, 0, 0],
                     [1, 2, 1]))
sobelBottom = np.array(([1, 2, 1],
                        [0, 0, 0],
                        [-1, -2, -1]))


def convolve_filter(kernel, path, filename, save_folder):
    img_src = cv2.imread(path, 0)
    # filter the source image
    img_rst = cv2.filter2D(img_src, -1, kernel)
    # save result image
    output_filename = save_folder + filename
    cv2.imwrite(output_filename, img_rst)
    title_origin = "Original image" + path
    title_result = "Result image" + path
    cv2.imshow(title_origin, img_src)
    cv2.imshow(title_result, img_rst)
    cv2.waitKey(0)
    cv2.destroyAllWindows();


if __name__ == '__main__':
    folder = "../img"
    # all file image
    images = os.listdir(folder)
    print(images[0])
    for i in range(0, len(images)):
        images_path = folder + "/" + images[i]
        convolve_filter(laplacian5, images_path, images[i], save_folder='save_output1/')
        convolve_filter(laplacian3, images_path, images[i], save_folder='save_output2/')
        convolve_filter(sobelLeft, images_path, images[i], save_folder='save_output3/')
        convolve_filter(sobelRight, images_path, images[i], save_folder='save_output4/')
        convolve_filter(sobelTop, images_path, images[i], save_folder='save_output5/')
        convolve_filter(sobelBottom, images_path, images[i], save_folder='save_output6/')
