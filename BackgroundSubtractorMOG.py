#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 21:50:54 2017

@author: fs
"""

import numpy as np
import cv2
cap = cv2.VideoCapture('test.avi')
#fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
fgbg = cv2.createBackgroundSubtractorMOG2()
while(1):
  ret, frame = cap.read()
  print(ret)
  k = cv2.waitKey(30) & 0xff
  if k == 27 or ret == False:
    break
  fgmask = fgbg.apply(frame)
  cv2.imshow('frame',fgmask)
  

cap.release()
cv2.destroyAllWindows()
