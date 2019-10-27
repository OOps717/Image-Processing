import cv2
import numpy as np

sq = np.zeros((300,300), dtype=np.uint8)
cv2.rectangle(sq, (50,50), (250,250), 255, -2)
cv2.imshow('sq', sq)
cv2.waitKey()

ellipse = np.zeros((300,300), dtype=np.uint8)
cv2.ellipse(ellipse, (150,150), (150,150), 30, 0, 180, 255, -1, cv2.LINE_8)
cv2.imshow('ellipse', ellipse)
cv2.waitKey()
# Bitwise operations should be in the same directions
b_and = cv2.bitwise_and(sq,ellipse)
b_or = cv2.bitwise_or(sq, ellipse)
b_xor = cv2.bitwise_xor(sq, ellipse)
b_not = cv2.bitwise_not(sq)

cv2.imshow('and', b_and)
cv2.waitKey()
cv2.imshow('or', b_or)
cv2.waitKey()
cv2.imshow('xor', b_xor)
cv2.waitKey()
cv2.imshow('not', b_not)
cv2.waitKey()

cv2.destroyAllWindows()