#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 17:25:32 2017

@author: fs
"""
'''
腐蚀：根据卷积核的大小靠近前景的所有像素都会被腐蚀
掉(变为 0),所以前景物体会变小,整幅图像的白色区域会减少。这对于去除
白噪声很有用,也可以用来断开两个连在一块的物体等。
总结：腐蚀会减少白色物体的面积


膨胀: 与腐蚀相反,与卷积核对应的原图像的像素值中只要有一个是 1,中心元
素的像素值就是 1。所以这个操作会增加图像中的白色区域(前景)。一般在去
噪声时先用腐蚀再用膨胀。因为腐蚀在去掉白噪声的同时,也会使前景对象变
小。

开运算: 先进性腐蚀再进行膨胀. 用于去除背景噪声

闭运算: 先膨胀再腐蚀。它经常被用来填充前景物体中的小洞,或者前景物体上的
小黑点。
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('open.png',0)
ret, bina = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

erosion = cv2.erode(bina,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


plt.subplot(231),plt.imshow(img,'gray'),plt.title('origin')
plt.subplot(232),plt.imshow(bina,'gray'),plt.title('binary')
plt.subplot(233),plt.imshow(erosion,'gray'),plt.title('erosion')
plt.subplot(234),plt.imshow(dilation,'gray'),plt.title('dilation')
plt.subplot(235),plt.imshow(opening,'gray'),plt.title('open')
plt.subplot(236),plt.imshow(closing,'gray'),plt.title('close')
