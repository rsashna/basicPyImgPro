"""
*Python file to make gaussian kernel and then blur image
*outputs blurred img
*
"""

import cv2
import math
import numpy as np
import gaussKernel

img =cv2.imread('Lenna.png')
r=5
h=np.zeros((r, r))

#python needs size of kernel
kernel = np.ones((r,r), np.uint8)

#own function in same folder
h=gaussKernel.gaussKernel(r)
imgOut = cv2.filter2D(img, -1, h)

#python needs size of kernel
kernel = np.ones((15,15), np.uint8)

#erode checks kernel if any px is dark, darkens current px
#dilate checks kernel if any px is light, lightens current px
imgOutE = cv2.erode(img, kernel, iterations=1)
imgOutD = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('image', img)
cv2.imshow('gaussianBlur', imgOut)
cv2.imshow('erode', imgOutE)
cv2.imshow('dilate', imgOutD)
print(np.matrix(h))
#wait for end key q
cv2.waitKey(0)
