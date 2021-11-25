import numpy as np
import cv2
import os


def box_blur_filter(path, filename):
    img_src = cv2.imread(path, 0)
    # prepare the 3x3 shaped filter
    kernel = np.array([[1, 1, 1],
                       [1, 1, 1],
                       [1, 1, 1]])

    # average filter
    kernel = kernel / sum(kernel)
    # filter the source image
    img_rst = cv2.filter2D(img_src, -1, kernel)
    # save result image
    output_filename = 'save_output/' + filename
    print(output_filename)
    cv2.imwrite(output_filename, img_rst)
    title_origin = "Original image box blur" + path
    title_result = "Result image box blur" + path
    cv2.imshow(title_origin, img_src)
    cv2.imshow(title_result, img_rst)
    cv2.waitKey(0)
    cv2.destroyAllWindows();

def gaussian_filter(path, filename):
    img_src = cv2.imread(path, 0)
    # prepare the 3x3 shaped filter
    gaussian = (1.0 / 16) * np.array([[1, 2, 1],
                                      [2, 4, 2],
                                      [1, 2, 1]])

    kernel = gaussian
    # filter the source image
    img_rst = cv2.filter2D(img_src, -1, kernel)
    # save result image
    output_filename = 'save_output2/' + filename
    print(output_filename)
    cv2.imwrite(output_filename, img_rst)
    title_origin = "Original image gaussian " + path
    title_result = "Result image gaussian" + path
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
        box_blur_filter(images_path, images[i])
        gaussian_filter(images_path, images[i])

