import numpy as np
import cv2

liveStream = cv2.VideoCapture(0)

while(True):
    # reading in each frame
    ret, frame = liveStream.read()
    # stream = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # stream = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Display the resulting frame
    # cv2.imshow('frame',stream)
    #show the frame
    cv2.imshow('frame', frame)
    #end stream
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# stop the camera
liveStream.release()
cv2.destroyAllWindows()
