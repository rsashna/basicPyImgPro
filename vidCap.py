import numpy as np
import cv2

liveStream = cv2.VideoCapture(0)

while(True):
    # reading in each frame
    ret, frame = liveStream.read()
    stream = cv2.applyColorMap(frame, cv2.COLORMAP_RAINBOW)

    """
    JET PARULA SPRING WINTER AUTUMN COOL(creepy) COLORMAP_RAINBOW
    """


    # Display the resulting frame
    # cv2.imshow('frame',stream)
    #show the frame
    cv2.imshow('frame', stream)
    #end stream
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# stop the camera
liveStream.release()
cv2.destroyAllWindows()
