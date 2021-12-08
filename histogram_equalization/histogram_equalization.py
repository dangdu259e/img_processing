# Cân bằng histogram của ảnh Gray và ảnh BGR bằng thư viện CV2

import cv2
import numpy as np
import matplotlib.pyplot as plt


# Đồ thị biểu diễn histogram của ảnh
def getHistogramGrap(img, title, number):
    # using numpy
    # hist: histogram
    # bins: 0-256

    plt.figure(number)

    hist, bins = np.histogram(img.flatten(), bins=256, range=[0, 256])
    plt.title(title)
    plt.xlabel('scale value')
    plt.ylabel('pixel')
    plt.xlim([0.0, 255.0])  # Số mức xám biểu thị trên trục
    plt.plot(hist)
    save_path = "./output_image/"
    save_name = str(title).replace(" ", "")
    save = save_path + save_name
    plt.savefig(save)


# Cân bằng histogram với ảnh gray và hiển thị
def equalization_histogram_gray_img(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_equalized = cv2.equalizeHist(img_gray)

    cv2.imshow('Gray Image', img_gray)
    cv2.imshow('Image Equalized', img_equalized)
    cv2.imwrite("./output_image/img_equalized_Gray.png", img_equalized)
    getHistogramGrap(img_gray, "Histogram Origin Image Gray", 1)
    getHistogramGrap(img_equalized, "Histogram Equalized Img Gray", 2)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Cân bằng histogram với ảnh BRG và hiển thị
def equalization_histogram_BGR_img(img):
    # chuyển đổi BGR to HSV
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # equalization_histogram in V channels (V-Value: độ sáng của màu sắc)
    img_hsv[:, :, 2] = cv2.equalizeHist(img_hsv[:, :, 2])
    img_equalized = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow('Origin Img', img)
    cv2.imshow('Image Equalized', img_equalized)
    cv2.imwrite("./output_image/img_equalized_BGR.png", img_equalized)
    getHistogramGrap(img, "Histogram Origin Image BGR", 1)
    getHistogramGrap(img_equalized, "Histogram Equalization Img BGR", 2)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    path_1 = "./image/test2.png"
    img_1 = cv2.imread(path_1)
    equalization_histogram_gray_img(img_1)

    path_2 = "./image/low_contrast.png"
    img_2 = cv2.imread(path_2)
    equalization_histogram_BGR_img(img_2)
