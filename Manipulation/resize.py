import cv2
import numpy as np

img = cv2.imread('/home/oops/Desktop/OpenCV/images/input.jpg')
img_scaled1 = cv2.resize(img, (900,400), interpolation=cv2.INTER_AREA) # better for shrinking
img_scaled2 = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC) # good
img_scaled3 = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_NEAREST) #fastest
img_scaled4 = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_LINEAR) # good for zooming or up sampling (default)
img_scaled5 = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_LANCZOS4) # the best
img_scaled6 = cv2.resize(img, None, fx=0.75, fy=0.75)
cv2.imshow('area', img_scaled1)
cv2.waitKey()
cv2.imshow('cubic', img_scaled2)
cv2.waitKey()
cv2.imshow('nearest', img_scaled3)
cv2.waitKey()
cv2.imshow('linear', img_scaled4)
cv2.waitKey()
cv2.imshow('lanczos', img_scaled5)
cv2.waitKey()
cv2.imshow('resized', img_scaled6)
cv2.waitKey()
cv2.destroyAllWindows()