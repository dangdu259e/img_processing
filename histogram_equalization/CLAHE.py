import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading the image from the present directory
image = cv2.imread("F:\SourceCode\ImageProcessing\histogram_equalization\image\CLAHE_img.jpg")

# The initial processing of the image
# image = cv2.medianBlur(image, 3)
image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# The declaration of CLAHE
# clipLimit -> Threshold for contrast limiting
clahe = cv2.createCLAHE(clipLimit=2)
final_img = clahe.apply(image_bw)

cv2.imshow("original img", image_bw)
hist_image_bw, bins_image_bw = np.histogram(image_bw.flatten(), bins=256, range=[0, 255])

# Cân bằng histogram
img_equalized = cv2.equalizeHist(image_bw)
hist_Histogram_Img, bins_Histogram_Img = np.histogram(img_equalized.flatten(), bins=256, range=[0, 256])
cv2.imshow("Histogram Img Equalized", img_equalized)

# cân bằng CLAHE
cv2.imshow("CLAHE image", final_img)
hist_CLAHE_bw, bins_CLAHE_bw = np.histogram(final_img.flatten(), bins=256, range=[0, 255])

cv2.waitKey(0)
cv2.destroyAllWindows()

fig, ax = plt.subplots(3)
fig.suptitle('** Biểu đồ histogram **', fontsize=20)
plt.style.use('seaborn')

ax[0].plot(hist_image_bw)
ax[0].set_title('Ảnh gốc')

ax[1].plot(hist_Histogram_Img)
ax[1].set_title('Ảnh cân bằng histogram bình thường')

ax[2].plot(hist_CLAHE_bw)
ax[2].set_title('Ảnh sau CLAHE')

plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.8,
                    wspace=0.6,
                    hspace=0.8)
plt.show()
