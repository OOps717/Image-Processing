import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('/home/oops/Desktop/OpenCV/images/tobago.jpg')

histogram = cv2.calcHist([img], [0], None, [256], [0,256]) # second value to calculate histogram (0 - blue)
plt.hist(img.ravel(), 256, [0,256]); plt.show()

color = ('b', 'g', 'r')

for i, col in enumerate(color):
    histogram2 = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(histogram2, color = col)
    plt.xlim([0,256])

plt.show()

