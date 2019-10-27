import cv2
import numpy as np

# input = cv2.imread('/home/oops/Desktop/OpenCV/images/input.jpg')
# gray = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY)
# Instead of prev lines we can easily write
gray = cv2.imread('/home/oops/Desktop/OpenCV/images/tobago.jpg', 0)
cv2.imshow('gray', gray)
cv2.waitKey()
cv2.destroyAllWindows()