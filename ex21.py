import cv2
import numpy as np
image = cv2.imread('moto.jpg', cv2.IMREAD_GRAYSCALE)
la= np.float32([[-1, -1, -1],[-1, 8, -1],[-1, -1, -1]])
s= cv2.filter2D(image, -1, la)
cv2.imshow('Sharpened Image', s)
cv2.waitKey(0)
cv2.destroyAllWindows()
