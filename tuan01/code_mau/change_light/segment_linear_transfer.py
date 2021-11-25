# biến đổi tuyến tính từng khúc

from matplotlib import pyplot as plt
import numpy as np
import cv2


# Find pice-linear transfrom
def Stretch_value(I, a, b, Ga, Gb):
    if (0 <= I and I <= a):
        G = (Ga / a) * I
    elif (a < I and I <= b):
        G = ((Gb - Ga) / (b - a)) * (I - a) + Ga
    else:
        G = ((255 - Gb) / (255 - b)) * (I - b) + Gb
    return G


def Contrast_stretch(Image, a, b, Ga, Gb):
    for i in range(Image.shape[0]):
        for j in range(Image.shape[0]):
            Image[i, j] = Stretch_value(Image[i, j], a, b, Ga, Gb)
    return Image


def main():
    Image = cv2.imread("../../image/low_contract.jpg")
    gray_image = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
    # Initialize range
    # Look for a, b from histogram first!!!
    a = 100
    b = 230
    Ga = 0
    Gb = 255
    pixelValue_vec = np.vectorize(Stretch_value)
    # Contrast stretching
    contrast = pixelValue_vec(Image, a, b, Ga, Gb)
    cv2.imshow("Stretched contrast image", contrast)


if __name__ == '__main__':
    main()
