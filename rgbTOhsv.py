"""
 * Python script to change img to grey and display both
 *
 * usage: run as script
 * q to exit on window
"""
import sys
import cv2

img =cv2.imread('Lenna.png')
height, width, channels = img.shape
flag=cv2.COLOR_BGR2HSV
flagGREY=cv2.COLOR_BGR2GRAY
img2=cv2.cvtColor(img, flagGREY)
cv2.imshow('image', img)
cv2.imshow('image2', img2)
print (height)
c = cv2.waitKey(0)
if 'q' == chr(c & 255):
    QuitProgram()
