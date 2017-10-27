#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 20:14:10 2017

@author: fs
"""

import cv2
import numpy as np
img = cv2.imread('lunkuo1.png')

ret,thresh = cv2.threshold(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),127,255,0)
_,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)#得到轮廓信息
cnt = contours[0]#取第一条轮廓

#%% 计算轮廓的旋转矩阵
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img,[box],0,(0,0,255),2)

#计算轮廓的直边界矩阵
x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


#计算轮廓外接圆
(rx,ry),radius = cv2.minEnclosingCircle(cnt)
center = (int(rx),int(ry))
radius = int(radius)
cv2.circle(img,center,radius,(255,0,0),2)

#计算轮廓外接椭圆
ellipse = cv2.fitEllipse(cnt)
cv2.ellipse(img,ellipse,(125,125,255),5)
    
#轮廓拟合曲线
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)
cv2.imshow('lunkuo1',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
