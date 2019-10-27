import cv2
import numpy as np

img = cv2.imread('/home/oops/Desktop/OpenCV/images/input.jpg')

smaller = cv2.pyrDown(img)
larger = cv2.pyrUp(smaller)

cv2.imshow('original', img)
cv2.imshow('smaller', smaller)
cv2.imshow('larger', larger)

cv2.waitKey()
cv2.destroyAllWindows()