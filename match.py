#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 22:28:10 2017

@author: fs
"""

import cv2
import numpy as np
img1 = cv2.imread('apple.jpg',0)
img2 = cv2.imread('orange.jpg',0)
ret, thresh1 = cv2.threshold(img1, 127, 255,cv2.THRESH_BINARY_INV)
ret, thresh2 = cv2.threshold(img2, 127, 255,cv2.THRESH_BINARY_INV)
_,contours1,hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt1 = contours1[0]
_,contours2,hierarchy = cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt2 = contours2[0]
ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print (ret)
