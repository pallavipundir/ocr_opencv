import face_recognition
import cv2

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("/home/pallavi/F/Softwares/Iphone/pan/pc1.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces([obama_face_encoding], face_encoding)
            name = "Unknown"

            if match[0]:
                name = "Barack"

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imwrite("/home/pallavi/Desktop/Video.jpg",frame)
# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()






import cv2
from cv2 import *
import numpy as np

face_cascade = cv2.CascadeClassifier('/home/pallavi/E/OCR_Work/ocr_opencv/Haarcascade/haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('Haarcascade/haarcascade_eye.xml')

capture= cv2.VideoCapture(0)
while True:
    ret,img=capture.read()   #capture frame by frame
    if ret:
        gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray=gray[y:y+h,x:x+w]
            roi_color=img[y:y+h,x:x+w]
        #eyes=eye_cascade.detectMultiScale(roi_gray)

        #for (ex,ey,ew,eh) in eyes:
          #  cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
        cv2.imshow('Our face extractor',img)
        k=cv2.waitKey(30) & 0xff   # Why 0xFF? We only want the lowest byte. This is mainly for cross-platform safety.j
        if k==2:   # Escape key
            break
    
capture.release()
cv2.destroyAllWindows()



 k= cv2.waitKey(1) & 0xFF == ord('q')      #cv2.waitKey(30) & 0xff
        if k:                                   #if k==2: 
            break
    