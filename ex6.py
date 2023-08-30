import cv2 as cv
cap=cv.VideoCapture('video.mp4')
i=0
while True:
    isTrue,frame=cap.read()
    cv.imshow('Video',frame)
    if(i<250):
        cv.waitKey(100)
    else:
        cv.waitKey(1)
    i+=1

