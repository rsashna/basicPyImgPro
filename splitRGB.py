import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Lenna.png')
imgO=img;
b,g,r = cv2.split(imgO)
# imgO = cv2.merge([r,g,b])

imgO = img[:,:,::-1]

# b,g,r = cv2.split(img) #can also be done like this
# img2 = cv2.merge([r,g,b])
# b = img[:,:,0]
# g = img[:,:,1]
# r = img[:,:,2] #alt split channels
# img2 = img[:,:,::-1] #ALT conversion to RGB
# cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # alt to convert colourspaces

titles = ['Original Image', 'Blue Channel',
            'Green Channel', 'Red Channel']
images = [imgO, b, g, r]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
