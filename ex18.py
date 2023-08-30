
import cv2
image=cv2.imread("moto.jpg")
edge=cv2.Sobel(image,-1,dx=0,dy=2,ksize=1)
cv2.imshow('edgeImage',edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
