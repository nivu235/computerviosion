#to convert color image to erosion
import cv2
import numpy as np
k=np.ones((5,5),np.uint8)
image=cv2.imread("nive.jpg")
cv2.imshow('Original Image',image)
edge=cv2.Canny(image,100,150)

erode=cv2.erode(image,k)
cv2.imshow('erode',erode)
cv2.waitKey(0)
cv2.destroyAllWindows()
