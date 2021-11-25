# 5. Cân bằng Histogram
import numpy as np


def histogram_compute(Image):
    # Student have to complete this by themselves
    return 0


def user_equal_hist(Image):
    hist = histogram_compute(Image)
    new_img = np.zeros(Image.shape)
    # to calculate cumulative sum of histogram
    # instead, we can use numpy.cumsum
    cumulator = np.zeros_like(hist, np.float64)
    for i in range(len(cumulator)):
        cumulator[i] = hist[:i].sum()
    # print(cumulator)
    new_hist = (cumulator - cumulator.min()) / (cumulator.max() - cumulator.min()) * 255
    new_hist = np.uint8(new_hist)
    h, w = Image.shape[:2]
    for i in range(h):
        for j in range(w):
            new_img[i, j] = new_hist[Image[i, j]]
    return new_img
