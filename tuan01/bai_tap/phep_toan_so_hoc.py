# Cộng ảnh:
# a) 7_1.png +7_2.png;  7.png + 7_3.png + 7_4.png
# b)  ISIC_1.jpg + ISIC_2.png
# c) 1-500x250-3.jpg với trọng 0.6 và 2-500x250-2.jpg  với trọng 0.4
#
#
# Trừ ảnh:
# a) cups_three_bw.png - cups_one_bw.png
#
# c) Background_foreground.png - background.png

import cv2

img71 = cv2.imread('../image/7_1.png')
img72 = cv2.imread('../image/7_2.png')
img7 = cv2.imread('../image/7.png')
img73 = cv2.imread('../image/7_3.png')
img74 = cv2.imread('../image/7_4.png')
imgISIC_1 = cv2.imread('../image/ISIC_1.jpg')
imgISIC_2 = cv2.imread('../image/ISIC_2.png')
imgBackground_foreground = cv2.imread('../image/Background_foreground.png')
imgbackground = cv2.imread('../image/background.png')
imgcups_three_bw = cv2.imread('../image/cups_three_bw.png')
imgcups_one_bw = cv2.imread('../image/cups_one_bw.png')
# Cộng ảnh
# a phần 1
imga1 = cv2.add(img71, img72)
cv2.imshow('Addition Image imga1', imga1)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

# a phần 2
imga2_temp = cv2.add(img7, img73)
imga2 = cv2.add(imga2_temp, img74)
cv2.imshow('Addition Image imga2', imga2)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

# b
imgISIC_1 = cv2.cvtColor(imgISIC_1, cv2.COLOR_BGR2GRAY)
imgISIC_2 = cv2.cvtColor(imgISIC_2, cv2.COLOR_BGR2GRAY)
imgc = cv2.add(imgISIC_1, imgISIC_2)
cv2.imshow('Addition Image imgb', imgc)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

# c


# trừ ảnh
# a
imga_2 = cv2.subtract(imgcups_three_bw, imgcups_one_bw)
cv2.imshow('Subtracted Image imga_2', imga_2)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

# b
imgb_2 = cv2.subtract(imgBackground_foreground, imgbackground)
cv2.imshow('Subtracted Image imgb_2', imgb_2)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()


