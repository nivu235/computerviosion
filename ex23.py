import cv2
import numpy as np
image=cv2.imread('nive.jpg')
g=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
b=cv2.GaussianBlur(g,(5, 5),2)
unsharp=g-b
sharp=g+unsharp
cv2.imshow('Unsharp Mask', unsharp)
cv2.imshow('Sharpened', sharp)

