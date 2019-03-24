import cv2
#from __future__ import division
from PIL import Image
import matplotlib.pyplot as plt
from scipy import misc

import numpy as np
import os

def gauss(img,mean,var):
    x,y=np.shape(img)
    print(x,y)
    
    gauss=np.random.normal(mean,var**0.55,(x,y))
    gauss=gauss.reshape(x,y)
    
    print(gauss)  
  
    noise1=img+gauss
    noise1=noise1.astype(np.uint8)
    return noise1
#################################################
def speckle(img,mean,var):
    x,y=np.shape(img)
    print(x,y)

    spec=np.random.normal(mean,var,(x,y))
    spec=spec.reshape(x,y)

    print(spec)  
  
    noise2=img+img*spec
    noise2=noise2.astype(np.uint8)
    return noise2
##########################################################
def pois(img):
    x,y=np.shape(img)
    print(x,y)
  
    noise3 = np.random.poisson(img) 
    noise3=noise3.astype(np.uint8)
    return noise3
##########################################################
def sp(img,prob):
    
    noise3 = np.zeros(img.shape,np.uint8)
    threshold = 1 - prob 
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rad = np.random.random()
            if rad < prob:
                noise3[i][j] = 0
            elif rad > threshold:
                noise3[i][j] = 255
            else:
                noise3[i][j] = img[i][j]
    return noise3

 ######################################################   

def main():
    imgpath = '/home/adi/Desktop/'
    imgp = imgpath+'lena.jpg'

    img = cv2.imread(imgp,0)

    print(img)

    gauss_noise=gauss(img,0,100)
    pois_noise=pois(img)
    speckle_noise=speckle(img,0,0.18)
    sp_noise=sp(img,0.05)

    cv2.imshow('gaussian',gauss_noise)  #image display
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imshow('poisson',pois_noise)  #image display
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imshow('speckle',speckle_noise)  #image display
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imshow('salt&pepper',sp_noise)  #image display
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()
