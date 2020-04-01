import cv2
import math
import numpy as np

def convImg(img, h):

# function outim = convImg(img, h)

    # where h is the filter to be convolved with the image
    h=double(h)

    maxin=0
    [H, W] = size(h)
    padh=(H-1)/2
    padw=(W-1)/2
    [imgw, imgh] = size(img)
    temp=zeros(imgw,imgh)
    az=zeros(padw,imgh)
    azr=zeros(imgw+(2*padw),padh) # first row of cols

        imgpadded = [az img]
        imgpadded = [imgpadded az]
        imgpadded = [imgpadded azr]
        imgpadded = [azr imgpadded]

[imgwp, imghp] = size(imgpadded)

i = in range(1,w):
    j = in range(1,h):

    k = in range(1,W):
        l = in range(1,H):
            window(k,l)=double(imgpadded(k+i-1,l+j-1))# filter applied to window

    summG=sum(h, 'all')
    convWin=double(window.*h)# element wise conv
    summ=sum(convWin,'all')
    result=floor(summ/(summG))
    temp(i,j)=result

 outim = uint8(temp)

return temp
