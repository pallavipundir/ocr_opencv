# To ignore numpy errors:
#     pylint: disable=E1101
import cv2
import numpy as np

#import sys
face_cascade = cv2.CascadeClassifier('/home/pallavi/E/OCR_Work/ocr_opencv/libs/Haarcascade/haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('Haarcascade/haarcascade_eye.xml')

capture=cv2.VideoCapture(0)
while True:   
    ret,img=capture.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        #eyes=eye_cascade.detectMultiScale(roi_gray)

        #for (ex,ey,ew,eh) in eyes:
          #  cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    cv2.imshow('Our face extractor',img)
    k=cv2.waitKey(1) & 0xff
    if k==ord('s'):
        break
    
capture.release()
cv2.destroyAllWindows()
