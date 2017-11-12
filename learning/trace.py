import cv2
import numpy as np
cap=cv2.VideoCapture("2.mp4")
kernel1 = np.ones((2,2),np.uint8)
kernel2 = np.ones((2,2),np.uint8) 
while(1):
    # get every frame
    ret,frame=cap.read()
    # convert into HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # set yellow boundaries
    lower_yellow=np.array([10,100,100])
    upper_yellow=np.array([175,255,255])
    # set white boundaries
    lower_white=np.array([0,50,175])
    upper_white=np.array([50,100,255])    
    # calculate mask   
    mask1=cv2.inRange(hsv,lower_yellow,upper_yellow)
    mask2=cv2.inRange(hsv,lower_white,upper_white)
    
    #mask1 = cv2.erode(mask1,kernel2,iterations = 3)
    #mask = cv2.dilate(mask,kernel1,iterations = 2)
    
    # mask
    res1=cv2.bitwise_and(frame,frame,mask=mask1)
    res2=cv2.bitwise_and(frame,frame,mask=mask2)
    #resize
    frame = cv2.resize(frame,(400,300))
    res1 = cv2.resize(res1,(400,300))
    res2 = cv2.resize(res2,(400,300))    
    img = np.hstack((frame,res1,res2))
    # show
    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    cv2.imshow('compare', img)
    k=cv2.waitKey(5)&0xFF
    if k==27:
        break
    # close windows
cv2.destroyAllWindows()
