import cv2
import numpy as np
image = cv2.imread('moto.jpg')
g = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
b = cv2.GaussianBlur(g, (5, 5), 2)
high1= g - b
high2= g + 2.0 * high1
s= np.clip(high2, 0, 255).astype(np.uint8)
cv2.imshow('Sharpened',s)


