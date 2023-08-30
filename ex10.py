import cv2
import numpy as np
k=np.ones((5,5),np.uint8)
img=cv2.imread('nive.jpg')
imga=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("nive",imga)
cv2.waitKey(0)
