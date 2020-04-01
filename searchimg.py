"""
*Python code to check for
*image match in ryersonlogo
"""

import cv2
import math
import numpy as np
import gaussKernel

img =cv2.imread('ryelogo.jpg')
filt = cv2.imread('searchr.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
filt = cv2.cvtColor(filt, cv2.COLOR_BGR2GRAY)
h, w = filt.shape[:-1]
#own function in same folder
h=filt
imgOut = cv2.filter2D(img, -1, filt)

found = cv2.matchTemplate(img, filt, cv2.TM_CCOEFF_NORMED)
threshold = .8
loc = np.where(found >= threshold)
for pt in zip(*loc[::-1]):  # Switch collumns and rows
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imwrite('Found it', img)

#python needs size of kernel
kernel = np.ones((15,15), np.uint8)


cv2.imshow('image', img)
cv2.imshow('findMatch', imgOut)
# print(np.matrix(h))
#wait for end key q
cv2.waitKey(0)
