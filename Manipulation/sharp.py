import cv2
import numpy as np

img = cv2.imread('/home/oops/Desktop/OpenCV/images/input.jpg')
ker_sharp = np.array([[-1,-1,-1],
                      [-1,10,-1],
                      [-1,-1,-1]])
sharp = cv2.filter2D(img, -1, ker_sharp)
cv2.imshow('sharped', sharp)
cv2.waitKey()
cv2.destroyAllWindows()