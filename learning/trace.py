import cv2
import numpy as np
cap=cv2.VideoCapture(0)
a = 0
while(1):
    # ��ȡÿһ֡
    ret,frame=cap.read()
    # ת����HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # �趨��ɫ����ֵ
    lower_blue=np.array([0,50,25])
    upper_blue=np.array([255,255,255])
    # ������ֵ������ģ
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    # ��ԭͼ�����ģ����λ����
    res=cv2.bitwise_and(frame,frame,mask=mask)
    # ��ʾͼ��
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(5)&0xFF
    if k==27:
        break
    a += 1
    # �رմ���
cv2.destroyAllWindows()
