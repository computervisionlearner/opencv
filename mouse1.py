#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:36:48 2017

@author: fs
"""

import cv2
events=[i for i in dir(cv2) if 'EVENT'in i]
print( events )#查看所有的鼠标事件

'''

    CV_EVENT_MOUSEMOVE      =0,   //鼠标移动
    CV_EVENT_LBUTTONDOWN    =1,   //按下左键
    CV_EVENT_RBUTTONDOWN    =2,   //按下右键
    CV_EVENT_MBUTTONDOWN    =3,   //按下中键
    CV_EVENT_LBUTTONUP      =4,   //放开左键
    CV_EVENT_RBUTTONUP      =5,   //放开右键
    CV_EVENT_MBUTTONUP      =6,   //放开中键
    CV_EVENT_LBUTTONDBLCLK  =7,   //左键双击
    CV_EVENT_RBUTTONDBLCLK  =8,   //右键双击
    CV_EVENT_MBUTTONDBLCLK  =9,   //中键双击
    CV_EVENT_MOUSEWHEEL     =10,  //滚轮滚动
    CV_EVENT_MOUSEHWHEEL    =11   //横向滚轮滚动
    CV_EVENT_FLAG_LBUTTON   =1,   //左键拖拽
    CV_EVENT_FLAG_RBUTTON   =2,   //右键拖拽
    CV_EVENT_FLAG_MBUTTON   =4,   //中键拖拽
    CV_EVENT_FLAG_CTRLKEY   =8,   //按住CTRL拖拽
    CV_EVENT_FLAG_SHIFTKEY  =16,  //按住Shift拖拽
    CV_EVENT_FLAG_ALTKEY    =32   //按住ALT拖拽

'''

import cv2
import numpy as np
#mouse callback function
def draw_circle(event,x,y,flags,param):

  if event== cv2.EVENT_MOUSEMOVE and flags ==33:
      cv2.circle(img,(x,y),10,(255,0,0),-1)
# 创建图像与窗口并将窗口与回调函数绑定
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
  cv2.imshow('image',img)
  if cv2.waitKey(20)&0xFF==27:
    break
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
