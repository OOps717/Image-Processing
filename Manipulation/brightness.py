import cv2
import numpy as np

img = cv2.imread('/home/oops/Desktop/OpenCV/images/input.jpg')
M = np.ones(img.shape, dtype=np.uint8) * 175 # multiplication must be bigger than 1
added = cv2.add(img, M) # !!! the two arguments should be the same dimension
cv2.imshow('added', added)
cv2.waitKey()

subtracted = cv2.subtract(img,M)
cv2.imshow('sub', subtracted)
cv2.waitKey()

cv2.destroyAllWindows()