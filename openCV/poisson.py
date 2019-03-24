import cv2
import numpy as np


def pois(img):
    x,y=np.shape(img)
    print(x,y)
  
    noise = np.random.poisson(img) 
    noise=noise.astype(np.uint8)
    return noise

def main():
    imgpath = '/home/adi/Desktop/'
    imgp = imgpath+'lena.jpg'
    img=cv2.imread(imgp,0)
    
    print(img)

    noise=pois(img)
    print(noise)
    
    cv2.imshow('x',noise)  #image display
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()