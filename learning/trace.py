import cv2
import numpy as np
cap=cv2.VideoCapture("2.mp4")
kernel1 = np.ones((2,2),np.uint8)
kernel2 = np.ones((2,2),np.uint8) 
while(1):
    # 获取每一帧
    ret,frame=cap.read()
    # 转换到HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # 设定黄色的阈值
    lower_yellow=np.array([10,100,100])
    upper_yellow=np.array([175,255,255])
    # 设定白色的阈值
    lower_white=np.array([15,15,150])
    upper_white=np.array([100,255,255])    
    # 根据阈值构建掩模   
    mask1=cv2.inRange(hsv,lower_yellow,upper_yellow)
    mask2=cv2.inRange(hsv,lower_white,upper_white)
    
    #mask1 = cv2.erode(mask1,kernel2,iterations = 3)
    #mask = cv2.dilate(mask,kernel1,iterations = 2)
    
    # 对原图像和掩模进行位运算
    res1=cv2.bitwise_and(frame,frame,mask=mask1)
    res2=cv2.bitwise_and(frame,frame,mask=mask2)
    #resize
    frame = cv2.resize(frame,(400,300))
    res1 = cv2.resize(res1,(400,300))
    res2 = cv2.resize(res2,(400,300))    
    img = np.hstack((frame,res1,res2))
    # 显示图像
    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    cv2.imshow('compare', img)
    k=cv2.waitKey(5)&0xFF
    if k==27:
        break
    # 关闭窗口
cv2.destroyAllWindows()
