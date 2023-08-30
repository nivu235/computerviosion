#to convert color image to canny edge detection
import cv2
image=cv2.imread("samuel.jpeg")
edge=cv2.Canny(image,200,300)
cv2.imshow('edgeImage',edge)

