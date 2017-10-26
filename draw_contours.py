#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 21:40:07 2017

@author: fs
绘制轮廓
函数 cv2.findContours() 有三个参数,第一个是输入图像,第二个是
轮廓检索模式,第三个是轮廓近似方法。返回值有三个,第一个是图像,第二个
是轮廓,第三个是(轮廓的)层析结构。轮廓(第二个返回值)是一个 Python
列表,其中存储这图像中的所有轮廓。每一个轮廓都是一个 Numpy 数组,包
含对象边界点(x,y)的坐标。
函数 cv2.drawContours() 可以被用来绘制轮廓。它可以根据你提供
的边界点绘制任何形状。它的第一个参数是原始图像,第二个参数是轮廓,一
个 Python 列表。第三个参数是轮廓的索引(在绘制独立轮廓是很有用,当设
置为 -1 时绘制所有轮廓)。接下来的参数是轮廓的颜色和厚度等
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('apple.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,th = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite('bin.jpg',th)

#image = th
image, contours, hierarchy = cv2.findContours(th,
                                cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

img = cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imwrite('bianyuan.jpg',img)
