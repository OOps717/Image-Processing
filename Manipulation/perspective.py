import cv2
import numpy as np

img = cv2.imread('/home/oops/Desktop/OpenCV/images/scan.jpg')
cv2.imshow('Orig', img)
cv2.waitKey()

p_A = np.float32([[320,15], [700,215], [85,610], [530,780]])
p_B = np.float32([[0,0], [420,0], [0,594], [420,594]])

M = cv2.getPerspectiveTransform(p_A, p_B)

warped = cv2.warpPerspective(img, M, (420, 594))

cv2.imshow('Perspective', warped)
cv2.waitKey()
cv2.destroyAllWindows()