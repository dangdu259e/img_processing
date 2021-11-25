import numpy as np


# Biến đổi gamma - sử dụng hàm mũ


def adjust_image_gamma(image, gamma=1.0):
    image_new = np.power(image, gamma)  # compute I^gamma
    max_val = np.max(image_new.ravel())  # compute max value of new image
    c = 255 / max_val  # compute c, maximum gray level is 255
    image_new = image_new * c  # G = c.I^gamma
    image_new = image_new.astype(np.uint8)  # set type to un integer 8 bits
    return image_new

# Ví dụ như ảnh CG_gray.png ở trên, nếu ta chọn γ = 0.35 sẽ cho kết quả như sau
