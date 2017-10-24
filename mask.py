#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 20:22:43 2017

@author: fs
"""

import cv2

model = cv2.imread('s1.jpg')
model1 = model.copy()
logo = cv2.imread('test.png')

rows, cols,_ = logo.shape

gray_logo = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(gray_logo,175,255,cv2.THRESH_BINARY) #get binary image
mask_inv = cv2.bitwise_not(mask)                             #get inv_binary image

roi = model[:rows,:cols,:]


#找到logo的轮廓
wakeng = cv2.bitwise_and(roi,roi,mask = mask)

#找到logo的前景
tiankeng = cv2.bitwise_and(logo,logo,mask = mask_inv)

goal = cv2.add(wakeng,tiankeng)

model[:rows,:cols] = goal

model1[:rows,:cols] = cv2.add(0.5*model1[:rows,:cols],0.5*logo)
cv2.imshow('model',model)
cv2.imshow('model1',model1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
