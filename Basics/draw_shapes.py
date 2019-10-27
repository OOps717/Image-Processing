import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

cv2.line (img, (0,0), (511,511), (255,127,0), 5)
cv2.line (img, (0,511), (511,0), (255,127,0), 5)
cv2.imshow('Line',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = np.zeros((512,512,3), np.uint8)
cv2.rectangle(img, (100,100), (400,400), (255,255,0), -1)
cv2.imshow('Rectangle',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = np.zeros((512,512,3), np.uint8)
cv2.circle(img, (255,255), 200, (255,255,0), -1, cv2.LINE_8)
cv2.imshow('Circle',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = np.zeros((512,512,3), np.uint8)
pts = np.array([[100,400],[100,100],[300,100],[100,100],[100,200],[200,200]])
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], False, (0,0,255), 3, cv2.LINE_8) #False - not closed
cv2.imshow('Polygon',img)
cv2.waitKey(0)
cv2.destroyAllWindows()