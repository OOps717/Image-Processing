import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

img_bw = np.zeros((512,512), np.uint8)
cv2.imshow('Black and White (Color)',img)
cv2.imshow('Black and White (B&W)',img_bw)

cv2.waitKey(0)
cv2.destroyAllWindows() 