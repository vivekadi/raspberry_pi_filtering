import cv2
import numpy as np
import os

def speckle(img,mean,var):
    x,y=np.shape(img)
    print(x,y)

    spec=np.random.normal(mean,var,(x,y))
    spec=spec.reshape(x,y)

    print(spec)  
  
    noise2=img+img*spec
    noise2=noise2.astype(np.uint8)
    return noise2

def main():
    imgpath = '/home/adi/Desktop/'
    imgp = imgpath+'lena.jpg'
    img=cv2.imread(imgp,0)
    
    print(img)

    noise=speckle(img,0,0.1)
    print(noise)
    
    cv2.imshow('x',noise)  #image display
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()