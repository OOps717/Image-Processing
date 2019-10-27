import cv2
import numpy as np

img = cv2.imread('/home/oops/Desktop/OpenCV/images/input.jpg')
h, w = img.shape[:2]
start_row, start_col = int(h*0.25), int(w*0.25)
end_row, end_col = int(h*0.75), int(w*0.75)

cropped = img[start_row:end_row, start_col:end_col]
cv2.imshow('cropped', cropped)

cv2.waitKey()
cv2.destroyAllWindows()
