import numpy as np
import cv2
a=input("enter slow or fast motion of video) 
cap=cv2.VideoCapture(0)
f=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('n.mp4',f,20.0,(640,480))
if(a=="fast"):                   
    while True:
        isTrue,frame=cap.read()
        cv2.imshow('Video',frame)
        out.write(frame)
        if cv2.waitKey(100) & 0xFF==ord('d'):
            break
else:
    while True:
        isTrue,frame=cap.read()
        cv2.imshow('Video',frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF==ord('d'):
            break
cap.release()
out.release()
cv2.destroyAllWindows()
