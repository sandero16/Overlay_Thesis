import cv2
import numpy as np

# Reading the input image
img = cv2.imread('probe_all_white.jpeg', 0)

# Taking a matrix of size 5 as the kernel
kernel = np.ones((5, 5), np.uint8)

# The first parameter is the original image,
# kernel is the matrix with which image is
# convolved and third parameter is the number
# of iterations, which will determine how much
# you want to erode/dilate a given image.
for i in range(10):
    dilation_factor = i
    img_erosion = cv2.erode(img, kernel, iterations=dilation_factor)
    img_dilation = cv2.dilate(img, kernel, iterations=dilation_factor)

    cv2.imwrite('newErosion_'+ str(dilation_factor) + '.jpeg', img_erosion)

cv2.waitKey(0)