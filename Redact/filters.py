import cv2
import numpy as np

def sketch (img, select):

    if select == 1: 
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # Clean up image
        img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
        #Get edges
        canny_edge = cv2.Canny(img_gray_blur, 10, 60)
        #Inver binarize
        ret, mask = cv2.threshold(canny_edge, 70, 255, cv2.THRESH_BINARY_INV)
        return mask
    elif select == 2: # R = B
        B, G, R = cv2.split(img)
        merged = cv2.merge([R,G,B])
        return merged
    elif select == 3: # Negative
        B, G, R = cv2.split(img)
        merged = cv2.merge([255-R,255-G,255-B])
        return merged
    elif select == 4: # Gamma Correction
        lookUpTable = np.empty((1,256), np.uint8)
        for i in range(256):
            lookUpTable[0,i] = np.clip(pow(i / 255.0, 1/2.2) * 255.0, 0, 255)
        res = cv2.LUT(img, lookUpTable)
        return res
    elif select == 5: # Vertical blur
        vert = cv2.filter2D(img, -1, cv2.getGaussianKernel(100,15))
        return vert
    elif select == 6: # Horizontal blur
        hor = cv2.blur(img, (40,1))
        return hor

cap = cv2.VideoCapture(0)
select = input("Press the number to choose the certain filter:\n1 - Sketch\n2 - Blue = Red\n3 - Negative\n4 - Gamma Correction\n5 - Vertical blur\n6 - Horizontal blur\n")
select = int(select)
frameName = ['Scetch', 'Blue = Red', 'Negative', 'Gamma Correction', 'Vertical Blur', 'Horizontal Blur']
while True:
    ret, frame = cap.read()
    cv2.imshow(frameName[select-1], sketch(frame, select))
    if cv2.waitKey(1) == 27: # ESC pressed
        break

cap.release()
cv2.destroyAllWindows()