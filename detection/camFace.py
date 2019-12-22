import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv2


def detectAndDisplay(frame):
    
    # creating orb
    orb = cv2.ORB_create(1000, 1.2)
    
    lookUpTable = np.empty((1,256), np.uint8)

    # Gamma correction
    for i in range(256):
        lookUpTable[0,i] = np.clip(pow(i / 255.0, 1/1.5) * 255.0, 0, 255)
    frame = cv2.LUT(frame, lookUpTable)

    # gray scaling our frame
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)
    
    # detecting face
    face_cascade = cv2.CascadeClassifier('/home/oops/Desktop/OpenCV/Haarcascades/haarcascade_frontalface_default.xml')    
    faces = face_cascade.detectMultiScale(frame_gray,1.3,3) 
    
    # downloading sample image and detecting face
    image = cv2.imread('/home/oops/Desktop/OpenCV/images/me.jpg', 0)   
    faces_2 = face_cascade.detectMultiScale(image,1.3,3)

    # cropping out the face from the sample image
    for (x,y,w,h) in faces_2:
        cropped_2 = image[y:y+h,x:x+w]
    (kp2, des2) = orb.detectAndCompute(cropped_2, None)

    if faces is not ():
        # cropping out the face from the frame
        for (x,y,w,h) in faces:
            cropped = frame_gray[y:y+h,x:x+w]
        (kp1, des1) = orb.detectAndCompute(cropped, None)   
        
        # matching two faces
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1,des2)

        # sorting by distance
        matches = sorted(matches, key=lambda val: val.distance)
        # drawing matches
        img = cv2.drawMatches(cropped, kp1, cropped_2, kp2, matches[:10],None, flags=2)
        
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 1, lineType=8)
        return frame, len(matches), img

    else:
        return frame, 0, 0


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        fr, matches, img = detectAndDisplay(frame)

        output_string = "Matches = " + str(matches)
        cv2.putText(fr, output_string, (fr.shape[0]//3,fr.shape[1]//10), cv2.FONT_HERSHEY_COMPLEX, 1, (75, 163, 41), 2)

        if matches > 200 and matches != 0:
            plt.imshow(img)
            plt.show()

        cv2.imshow('Detection', fr)
        if cv2.waitKey(1) == 27: # ESC pressed
            break

    cap.release()
    cv2.destroyAllWindows()