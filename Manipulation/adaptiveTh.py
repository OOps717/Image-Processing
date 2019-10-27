import cv2
import numpy as np

img = cv2.imread('/home/oops/Desktop/OpenCV/images/Origin_of_Species.jpg', 0)

_, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('BINARY', th)
cv2.waitKey()

th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
cv2.imshow('Adaptive_Mean', th1)
cv2.waitKey()

_, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('OTSU', th2)
cv2.waitKey()

gaussian = cv2.GaussianBlur(img, (5,5), 0)
_, th3 = cv2.threshold(gaussian, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Gaussian OTSU', th3)
cv2.waitKey()

cv2.destroyAllWindows()

