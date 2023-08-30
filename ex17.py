
import cv2
image=cv2.imread("moto.jpg")
edge=cv2.Sobel(image,cv2.CV_64F,dx=1,dy=0)
cv2.imshow('edgeImage',edge)

