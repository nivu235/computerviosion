import cv2
import numpy as np
image = cv2.imread('moto.jpg')
la= np.float32([[0, 1, 0],[1, -4, 1],[0, 1, 0]])
s= cv2.filter2D(image, -1, la)
cv2.imshow('Sharpened Image', s)
cv2.waitKey(0)
cv2.destroyAllWindows()
