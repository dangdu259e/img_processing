# Bai 03: Tao mot so hieu ung emboss filter
import numpy as np
import cv2
import os
emboss = np.array(
    [[-2, -1, 0],
     [-1, 1, 1],
     [0, 1, 2]])

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
        convolve_filter(emboss, images_path, images[i], save_folder='save_output1/')