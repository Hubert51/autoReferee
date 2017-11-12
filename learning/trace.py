import cv2
import numpy as np
cap=cv2.VideoCapture("2.mp4")
kernel1 = np.ones((1,2),np.uint8)
kernel2 = np.ones((1,2),np.uint8) 
while(1):
    # get every frame
    ret,frame=cap.read()
    frame = cv2.resize(frame,(640,360))
    # convert into HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # set yellow boundaries
    lower_yellow=np.array([10,20,210])
    upper_yellow=np.array([255,255,255])
    # set white boundaries
    lower_white=np.array([15,50,100])
    upper_white=np.array([100,100,255])     
    # set white center line
    lower_white2=np.array([0,0,215])
    upper_white2=np.array([200,18,255])    
    # calculate mask
    #ball
    mask1=cv2.inRange(hsv,lower_yellow,upper_yellow)
    #white boundaries
    mask2=cv2.inRange(hsv,lower_white,upper_white)
    #white center line
    mask3=cv2.inRange(hsv,lower_white2,upper_white2)
    mask2 = cv2.dilate(mask2,kernel1,iterations = 2)
    mask3 = cv2.dilate(mask3,kernel1,iterations = 2)
    
    #total 
    
    #mask1 = cv2.bitwise_or()
    mask1 = cv2.bitwise_or(mask1,mask2)
    mask1 = cv2.bitwise_or(mask1,mask3)
    # mask
    #res1=cv2.bitwise_and(frame,frame,mask=mask1)
    
    # show
    cv2.imshow('compare', mask1)

    k=cv2.waitKey(1)&0xFF
    if k==27:
        break
    # close windows
cv2.destroyAllWindows()
