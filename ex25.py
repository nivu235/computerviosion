import cv2
import numpy as np
img= cv2.imread('moto.jpg', cv2.IMREAD_GRAYSCALE)
x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
y = cv2.Sobel(img, cv2.CV_64F, 0, 1)
g= np.sqrt(x ** 2 +y ** 2)
s=img+0.5* g
s= np.clip(s, 0, 255).astype(np.uint8)
cv2.imshow('Sharpened', s)

