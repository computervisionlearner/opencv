#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 22:35:20 2017

@author: fs
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('apple.jpg',0)
# 别忘了中括号 [img],[0],None,[256],[0,256] ,只有 mask 没有中括号
#hist1 = cv2.calcHist([img],[0],None,[256],[0,256])
hist,bins = np.histogram(img.flatten(),256,[0,255])
x = np.arange(0,256)
plt.subplot(121),plt.plot(x,hist),plt.ylim(0,),plt.title('s')
plt.subplot(122),plt.hist(img.flatten(),bins=256),plt.title('hist')
plt.show()
