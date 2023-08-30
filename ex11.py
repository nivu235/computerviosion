import cv2
import numpy as np
image =cv2.imread("nive.jpg")
t= np.float32([[1, 0, 50], [0, 1, 30]])
aff= cv2.warpAffine(image,t,(2000, 3000))
cv2.imshow('Affine Transformed Image', aff)
cv2.waitKey(0)
cv2.destroyAllWindows()

