import cv2
import numpy as np

img = cv2.imread('/home/oops/Desktop/OpenCV/images/input.jpg')
h, w = img.shape[:2]

rot = cv2.getRotationMatrix2D((w/2,h/2), 45, .5) # the last arg is the scale of the image (razmer)
rot_img = cv2.warpAffine(img, rot, (w,h))
cv2.imshow('rotated', rot_img)
cv2.waitKey()
cv2.destroyAllWindows()

# To rotate on 90 degree without making img go out of the board
# rotated = cv2.transpose(img)
# cv2.imshow('rotated_2', rotated)
# cv2.waitKey()
# cv2.destroyAllWindows()