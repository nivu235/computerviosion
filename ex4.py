#to convert color image to dilate
import cv2
import numpy as np
k=np.ones((3,3),np.uint8)
image=cv2.imread("nive.jpg")
cv2.imshow('Original Image',image)
edge=cv2.Canny(image,100,150)
d=cv2.dilate(edge,k)
cv2.imshow('Dilate',d)
cv2.waitKey(0)
cv2.destroyAllWindows()
