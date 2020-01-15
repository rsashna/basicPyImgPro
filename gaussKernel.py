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
    # print("xtshape",xt.shape)
    # print("xrshape",xr.shape)
    xt1=np.array(xt)
    # print("lsit?",xt1)

    for i in range(r):
        xt[i] = (fr*2-(i+fr))
        # # xt.append((fr*2-(i+fr)))
        # np.append(xt,(fr*2-(i+fr)))
        # print((fr*2-(i+fr)))

    print("xt array: ",xt)
    xt=abs(xt)
    x=xr-xt

    gauss=x.astype(float)
    print("gauss:",gauss)
    for i in range(len(gauss)):
        gauss[i] = (1/((math.sqrt(2*math.pi))*sig)) *math.exp(-1/2*((x[i])-(r+1))**2/sigSq)
    print("gauss2:",gauss)
    # gauss = np.array(gauss)
    gaussm=np.tile(gauss,(r,1))#wierd stuff here
    print("gauss3:",gaussm)
    # gaussw2d = np.multiply(gauss.transpose(),gaussm)
    gaussw2d=np.outer(gauss, gauss)
    print("gaussw2d:",gaussw2d)
    summ=gaussw2d.sum()
    print("summ",summ)
    gaussw2d = (1/summ)*(gaussw2d)
    print("gaussw2d:",gaussw2d, "end")
    # gaussmat = fspecial('gaussian',[5 5],sig)
    h=gaussw2d

    return h
