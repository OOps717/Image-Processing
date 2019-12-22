import cv2
import numpy as np
import six

def sketch (img, select):
    if select == 1: 
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # Clean up image
        img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
        #Get edges
        canny_edge = cv2.Canny(img_gray_blur, 10, 60)
        #Invert binarize
        _, mask = cv2.threshold(canny_edge, 50, 255, cv2.THRESH_BINARY_INV)
        
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
        kernel = np.ones((40,1), np.float32)/40
        horiz = cv2.filter2D(img,-1,kernel)
        return horiz
    elif select == 7:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 30, 200)
        _, contours, hiearchy = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        # for c in contours:
        #     x,y,w,h = cv2.boundingRect(c)
        #     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2,cv2.LINE_8) 
        cv2.drawContours(img, contours, -1, (0,255,0), 3)
        return img
    elif select == 8:

        lookUpTable = np.empty((1,256), np.uint8)
        for i in range(256):
            lookUpTable[0,i] = np.clip(pow(i / 255.0, 1/2.2) * 255.0, 0, 255)
        img = cv2.LUT(img, lookUpTable)

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gaussian = cv2.GaussianBlur(img, (7,7), 0)
        edged = cv2.Canny(gaussian, 30, 200)
        _, contours, hiearchy = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

        for c in contours:
        # Calculate accuracy as a percent of the contour perimeter
            accuracy = 0.03 * cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, accuracy, True)

            if len(approx) <=10:
                cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
        
        return img


select = int(six.moves.input("Press the number to choose the certain filter:\n1 - Sketch\n2 - Blue = Red\n3 - Negative\n4 - Gamma Correction\n5 - Vertical blur\n6 - Horizontal blur\n7 - Contours\n8-Approximate contours\n"))
cap = cv2.VideoCapture(0)
frameName = ['Scetch', 'Blue = Red', 'Negative', 'Gamma Correction', 'Vertical Blur', 'Horizontal Blur','Contours', 'Approximate','o']
while True:
    ret, frame = cap.read()
    cv2.imshow(frameName[select-1], sketch(frame, select))
    if cv2.waitKey(1) == 27: # ESC pressed
        break

cap.release()
cv2.destroyAllWindows()