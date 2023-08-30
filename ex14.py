import cv2
import numpy as np
img=cv2.imread('moto.jpg')
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[100,50],[300,0],[0,300],[300,300]])
h,s=cv2.findHomography(pts1,pts2)
im=cv2.warpPerspective(img,h,(6000,5000))
cv2.imshow('homgraphy image',im)
cv2.waitKey(0)                       
