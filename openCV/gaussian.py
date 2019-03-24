
import cv2
import numpy as np

def gauss(img):
    x,y=np.shape(img)
    print(x,y)
    
    mean=0
    var=200
    sigma=var**0.5
    gauss=np.random.normal(mean,sigma,(x,y))
    gauss=gauss.reshape(x,y)
    
    print(gauss)  
  
    noise=img+gauss
    noise=noise.astype(np.uint8)
    return noise
    
def main():
    imgpath = '/home/adi/Desktop/'
    imgp = imgpath+'lena.jpg'
    img=cv2.imread(imgp,0)
    
    print(img)

    noise=gauss(img)
    print(noise)
    
    cv2.imshow('x',noise)  #image display
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()
