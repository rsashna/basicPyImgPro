import cv2
import math
import numpy as np

def gaussKernel(r):

    # where r is the actual kernel size of gaussian
    fr=math.floor(r/2)
    sig = r/3
    sigSq=sig**2
    xr=r* np.ones((5,), dtype=int)
    xt=np.ones((r,), dtype=int)
    xt1=np.array(xt)

    for i in range(r):
        xt[i] = (fr*2-(i+fr))
    print("xt array: ",xt)
    xt=abs(xt)
    x=xr-xt

    gauss=x.astype(float)
    print("gauss:",gauss)
    for i in range(len(gauss)):
        gauss[i] = (1/((math.sqrt(2*math.pi))*sig)) *math.exp(-1/2*((x[i])-(r+1))**2/sigSq)

    gaussm=np.tile(gauss,(r,1))

    gaussw2d=np.outer(gauss, gauss)

    summ=gaussw2d.sum()
    if summ == 0:
        summ = 0.00001
    gaussw2d = (1/summ)*(gaussw2d)

    h=gaussw2d
    print("Gaussian filter:\n",gaussw2d, "\n-.-.-\n")

    return h
