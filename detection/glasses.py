import numpy as np
import cv2


def eyes_detect(frame):

    lookUpTable = np.empty((1,256), np.uint8)
    # Gamma correction
    for i in range(256):
        lookUpTable[0,i] = np.clip(pow(i / 255.0, 1/1.5) * 255.0, 0, 255)
    frame = cv2.LUT(frame, lookUpTable)

    face_classifier = cv2.CascadeClassifier('/home/oops/Desktop/OpenCV/Haarcascades/haarcascade_frontalface_default.xml')
    eye_classifier = cv2.CascadeClassifier('/home/oops/Desktop/OpenCV/Haarcascades/haarcascade_eye.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_classifier.detectMultiScale(gray, 1.3, 5)      # face detection

    if faces is not ():                                         # if face detected
        for (x,y,w,h) in faces: 
            eyes = eye_classifier.detectMultiScale(gray, 1.3)   # eyes detection
            if len(eyes) == 2:                                  # if 2 eyes are detected
                points = []
                radiuses = []
                for (ex,ey,ew,eh) in eyes:
                    points.append((ex + ew//2,ey + eh//2))      # appending center points
                    radiuses.append(int(round((ew + eh)*0.25))) # appending radiuses
                

                if radiuses[0] < radiuses[1]:                   # selecting the smallest radius
                    radius = radiuses[0]
                else:
                    radius = radiuses[1]

                for i in range(len(eyes)):                      
                    frame = cv2.circle(frame, points[i], radius, (255,127,0), 2) # drawing circles around the eyes on the face


                if points[1][0]-radiuses[1] - points[0][0]+radiuses[0] < 0:      # selecting the first circle from the left in order to draw the shortest line
                    cv2.line (frame, (points[1][0]+radiuses[1],points[0][1]), (points[0][0]-radiuses[0],points[1][1]), (255,127,0), 2)
                else:
                    cv2.line (frame, (points[0][0]+radiuses[0],points[0][1]), (points[1][0]-radiuses[1],points[1][1]), (255,127,0), 2)
    return frame


if __name__ == '__main__':
    
    cap = cv2.VideoCapture(0)

    while True:
        # capturing from the camera and flipping the image
        ret, frame = cap.read()
        frame = cv2.flip(frame,1) 

        # implementing out function
        frame = eyes_detect(frame)

        cv2.imshow('glasses', frame)
        if cv2.waitKey(1) == 27: # ESC pressed
            break

    cap.release()
    cv2.destroyAllWindows()