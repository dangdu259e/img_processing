# Cân bằng histogram

import numpy as np
import os
import cv2
import matplotlib.pyplot as plt


# compute histogram
def compute_hist(img):
    hist = np.zeros((256,), np.uint8)
    h, w = img.shape[:2]
    for i in range(h):
        for j in range(w):
            hist[img[i][j]] += 1
    return hist


def print_histogram(img, title, number):
    hist = compute_hist(img)
    plt.figure(number)
    plt.title(title)
    plt.xlabel('scale value')
    plt.ylabel('pixel')
    plt.xlim([0.0, 255.0])  # Số mức xám biểu thị trên trục
    plt.plot(hist)
    save_path = "./output_image_handle/"
    save_name = str(title).replace(" ", "")
    save = save_path + save_name
    plt.savefig(save)


# cân bằng histogram
def equal_hist(hist):
    cumulator = np.zeros_like(hist, np.float64)
    for i in range(len(cumulator)):
        cumulator[i] = hist[:i].sum()  # t(g)
    new_hist = (cumulator - cumulator.min()) / (cumulator.max() - cumulator.min()) * 255
    new_hist = np.uint8(new_hist)
    return new_hist


def equalization_histogram_gray_img(img):
    print_histogram(img, "Histogram Origin Image Gray", 1)
    cv2.imshow('Origin Image', img)

    hist = compute_hist(img).flatten()

    new_hist = equal_hist(hist)

    # change new_hist to img
    img_equalized = img
    h, w = img_equalized.shape[:2]
    for i in range(h):
        for j in range(w):
            img_equalized[i, j] = new_hist[img_equalized[i, j]]

    cv2.imshow('Image Equalized', img_equalized)
    cv2.imwrite("./output_image_handle/img_equalized_Gray.png", img_equalized)
    print_histogram(img_equalized, "Histogram Img Equalized Gray", 2)

    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def histogram_equalization_BGR(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    print_histogram(img, "Histogram Origin Image BGR", 1)
    cv2.imshow('Origin Image', img)

    # equalization_histogram in V channels (V-Value: độ sáng của màu sắc)

    hist = compute_hist(img_hsv[:, :, 2]).flatten()

    new_hist = equal_hist(hist)

    # change new_hist to img
    img_equalized = img_hsv
    img_equalized_v = img_equalized[:, :, 2]
    h, w = img_equalized_v.shape[:2]
    for i in range(h):
        for j in range(w):
            img_equalized_v[i, j] = new_hist[img_equalized_v[i, j]]
    img_equalized[:, :, 2] = img_equalized_v
    img_equalized = cv2.cvtColor(img_equalized, cv2.COLOR_HSV2BGR)

    cv2.imshow('Image Equalized', img_equalized)
    cv2.imwrite("./output_image_handle/img_equalized_BGR.png", img_equalized)
    print_histogram(img_equalized, "Histogram Img Equalized BGR", 2)

    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # test gray
    path_1 = "./image/test2.png"
    img_1 = cv2.imread(path_1)
    equalization_histogram_gray_img(img_1)

    # test rgb
    path_2 = "./image/low_contrast.png"
    img_2 = cv2.imread(path_2)
    histogram_equalization_BGR(img_2)
