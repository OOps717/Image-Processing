import cv2
import numpy as np

img = cv2.imread('/home/oops/Desktop/OpenCV/images/input.jpg', 0)
cv2.imshow('orig', img)
cv2.waitKey()

h, w = img.shape

sobel_x = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

cv2.imshow('Sobel X', sobel_x)
cv2.waitKey()

cv2.imshow('Sobel Y', sobel_y)
cv2.waitKey()

sobel_or = cv2.bitwise_or(sobel_x, sobel_y)
cv2.imshow('OR sobels', sobel_or)
cv2.waitKey()

lap = cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow('Laplacian', lap)
cv2.waitKey()

canny = cv2.Canny(img, 20, 160)
cv2.imshow('Canny', canny)
cv2.waitKey()

cv2.destroyAllWindows()

