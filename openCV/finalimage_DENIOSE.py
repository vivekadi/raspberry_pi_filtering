from  __future__ import division
import cv2
import numpy as np
def contra():
    img=cv2.imread("/home/keshav/Desktop/guass.jpeg",0)
    x,y=img.shape
    cv2.imshow("img original",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    q=int(input("enter q: "))
    for i in range(x-1):
        for j in range(y-1):
            summat=img[i:i+3,j:j+3]
            add=0.0
            add2=0.0
            add3=0.0
            for k in summat:
                for m in k:
                    p=float(m)
                    add2=add2+p**(q+1)
                    add3=add3+p**q
            img[i+1,j+1]=add2/add3
    cv2.imshow("img final",img)
    cv2.imwrite("/home/keshav/Desktop/contraharm.jpeg",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def harmonic():
    img=cv2.imread("/home/keshav/Desktop/guass.jpeg",0)
    x,y=img.shape
    cv2.imshow("img original",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    for i in range(x-1):
        for j in range(y-1):
            summat=img[i:i+3,j:j+3]
            add=0.0
            for k in summat:
                for m in k:
                    p=float(m)
                    if p==0:
                        continue
                    add=add+1/p
            img[i+1,j+1]=9/add
            
           
    cv2.imshow("img final",img)
    cv2.imwrite("/home/keshav/Desktop/har.jpeg",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def inversecontra():
    img=cv2.imread("/home/keshav/Desktop/guass.jpeg",0)
    x,y=img.shape
    cv2.imshow("img original",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    q=int(input("enter q: "))
    for i in range(x-1):
        for j in range(y-1):
            summat=img[i:i+3,j:j+3]
            add=1.0
            add2=0.0
            add3=0.0
            g=0.22222
            for k in summat:
                for m in k:
                    p=float(m)
                    if p==0:
                        continue
                    add=add*p
                    add2=add2+p**(q+1)
                    add3=add3+p**q
            img[i+1,j+1]=(add**g)*(add3/add2)
    cv2.imshow("img final",img)
    cv2.imwrite("/home/keshav/Desktop/centroidal.jpeg",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def centroidal():
    img=cv2.imread("/home/keshav/Desktop/guass.jpeg",0)
    x,y=img.shape
    cv2.imshow("img original",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    q=int(input("enter q: "))
    for i in range(x-1):
        for j in range(y-1):
            summat=img[i:i+3,j:j+3]
            add=0.0
            add2=0.0
            add3=0.0
            for k in summat:
                for m in k:
                    p=float(m)
                    add=add+p
                    add2=add2+p**(q+1)
                    add3=add3+p**q
            img[i+1,j+1]=9/(3*add)+(2*add2)/(3*add3)
    cv2.imshow("img final",img)
    cv2.imwrite("/home/keshav/Desktop/centroidal.jpeg",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def heron():
    img=cv2.imread("/home/keshav/Desktop/guass.jpeg",0)
    x,y=img.shape
    cv2.imshow("imgoriginal",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    for i in range(x-1):
        for j in range(y-1):
            add=0.0
            prod=1.0
            replace=0.0000000000
            summat=img[i:i+3,j:j+3]
            for k in summat:
                for m in k:
                    p=float(m)
                    add=p+add
                    prod=prod*p
            replace=2*add/27 +(prod**(1/9))/3
            img[i+1,j+1]=replace
    cv2.imshow("img final",img)
    cv2.imwrite("/home/keshav/Desktop/heron.jpeg",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

heron()
centroidal()
harmonic()
inversecontra()
contra()
def mse(f,x):
    f-x
    
