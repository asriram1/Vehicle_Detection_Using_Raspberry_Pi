# import libraries of python OpenCV 
import cv2
capture_frames = cv2.VideoCapture('videonew3.mp4')# capture frames from video recorded through raspberry pi 
car_casc = cv2.CascadeClassifier('cars.xml') # Trained XML classifier describes some features of the object, in this case cars, that we want to detect

while True: # loop runs if capturing has been initialized.

    ret, frames = capture_frames.read() # reads frames from a video
     
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) # function converts each frame to gray scale 
     
 
    cars = car_casc.detectMultiScale(gray, 1.1, 1)# MultiScale function detects cars of different sizes in the input images
     
    # for loop to create rectangles around each of the cars
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
 
   # imshow function to display frames in a window 
    cv2.imshow('video2', frames)
     
    # waitKey function waits for Esc key to stop
    if cv2.waitKey(33) == 27:
        break
 
#This de-allocates any associated memory usage
cv2.destroyAllWindows()
