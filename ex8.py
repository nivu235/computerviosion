import cv2
import numpy as np
k=np.ones((5,5),np.uint8)
img=cv2.imread('nive.jpg')
img=cv2.resize(img,(600,600))
cv2.imshow("nive",img)
cv2.waitKey(0)
