import cv2
import numpy as np

img = cv2.imread('/home/oops/Desktop/OpenCV/images/gradient.jpg')

ret , thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('binary', thresh1)
cv2.waitKey()

ret , thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('binary inv', thresh2)
cv2.waitKey()

ret , thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC) # Every pixel with value bigger than 127 now equal to 127
cv2.imshow('trunc', thresh3)
cv2.waitKey()

ret , thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO) # Every value less than 127 equal to 0 
cv2.imshow('to zero', thresh4)
cv2.waitKey()

ret , thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('to zero inv', thresh5)
cv2.waitKey()

cv2.destroyAllWindows()