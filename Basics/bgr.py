import cv2
import numpy as np

img = cv2.imread('/home/oops/Desktop/OpenCV/images/input.jpg')
B, G, R = img[0,0]
print(B,G,R)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print (gray[0,0])

# Converting to HueSaturationValue
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow('hsv',hsv)
# cv2.waitKey()
# cv2.imshow('hsv HUE',hsv[:,:,0])
# cv2.waitKey()
# cv2.imshow('hsv SATURATION',hsv[:,:,1])
# cv2.waitKey()
# cv2.imshow('hsv VALUE',hsv[:,:,2])
# cv2.waitKey()
# cv2.destroyAllWindows()

B, G, R = cv2.split(img) #convert automatically to grayscale component
# cv2.imshow('blue',B)
# cv2.imshow('green',G)
# cv2.imshow('red',R)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

merged = cv2.merge([B,G,R]) # we can add any value to one of the component
cv2.imshow('merged',merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

B, G, R = cv2.split(img) 
zeros = np.zeros(img.shape[:2], dtype = "uint8")
cv2.imshow('blue',cv2.merge([B,zeros,zeros]))  
cv2.waitKey(0)
cv2.destroyAllWindows() 