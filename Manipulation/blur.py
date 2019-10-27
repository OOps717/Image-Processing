import cv2
import numpy as np

img = cv2.imread('/home/oops/Desktop/OpenCV/images/elephant.jpg')  

kernel7 = np.ones((7,7), np.float32)/49 # Division for normalization 
blurred2 = cv2.filter2D(img, -1, kernel7)
cv2.imshow('filter', blurred2)
cv2.waitKey()

blurred1 = cv2.blur(img, (7,7)) # Averages the pixels in the box
cv2.imshow('box', blurred1)
cv2.waitKey()

gaussian = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow('gaussian', gaussian)
cv2.waitKey()

median = cv2.medianBlur(img, 7) # finds median value in the box
cv2.imshow('median', median)
cv2.waitKey()

bilateral = cv2.bilateralFilter(img, 7, 75, 75)
cv2.imshow('bilateral', bilateral)
cv2.waitKey()

deNoise = cv2.fastNlMeansDenoisingColored(img,None, 6, 6, 7, 21)
cv2.imshow('Fast and Means denoise', deNoise)
cv2.waitKey()

cv2.destroyAllWindows()
