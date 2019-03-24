import numpy as np
import random
import cv2

def sp(image,prob):
    
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

def main():
    imgpath = '/home/adi/Desktop/'
    imgp = imgpath+'lena.jpg'

    image = cv2.imread(imgp,0) # Only for grayscale image
    noise_img = sp(image,0.05)

    cv2.imshow('sp_noise.jpg', noise_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()


