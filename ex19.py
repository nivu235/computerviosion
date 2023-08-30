
import cv2
image=cv2.imread("nive.jpg")
edge=cv2.Sobel(image,cv2.CV_64F,dx=1,dy=1)
cv2.imshow('edgeImage',edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
