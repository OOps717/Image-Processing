import cv2
import numpy as np

img = cv2.imread('/home/oops/Desktop/OpenCV/images/input.jpg')
h, w = img.shape[:2]

quarter_h, quarter_w = h/4, w/4

T = np.float32([[1,0,quarter_w],[0,1,quarter_h]])
img_tr = cv2.warpAffine(img, T, (w,h))
cv2.imshow('not shifted', img)
cv2.imshow('shifted', img_tr)
cv2.waitKey()
cv2.destroyAllWindows()