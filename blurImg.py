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
h=gaussKernel.gaussKernel(r)
cv2.imshow('image', img)

print(np.matrix(h))
cv2.waitKey(0)

# cv2.imshow('image2', img2)
