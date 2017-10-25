#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:11:45 2017

@author: fs
"""

import cv2
import numpy as np

img=cv2.imread('s1.jpg')
rows,cols,channels = img.shape

def translation(img):
  
  
  M = np.float32([[1,0,100],[0,1,50]])
  dst = cv2.warpAffine(img,M,(cols,rows))
  return dst
  
  
def rotation(img):
  M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)#这种方法主要针对正方形，如果图像是长方形，则旋转之后会有部分损失
  dst = cv2.warpAffine(img,M,(cols,rows))
  
#  M = np.float32([[0,1,0],[-1,0,cols]])
#  dst = cv2.warpAffine(img,M,(rows,cols))#这种方法针对长方形图像，旋转之后不会有遮挡
  
  return dst

def affine(img):
  pts1 = np.float32([[50,50],[200,50],[50,200]])
  pts2 = np.float32([[10,100],[200,50],[100,250]])
  M = cv2.getAffineTransform(pts1,pts2)#2*2
  dst = cv2.warpAffine(img,M,(cols,rows))
  return dst

def perspective(img):
  pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
  pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
  M = cv2.getPerspectiveTransform(pts1,pts2)  #3*3
  dst = cv2.warpPerspective(img,M,(cols,rows))
  return dst

tran = translation(img)
rota = rotation(img)
affi = affine(img)
pers = perspective(img)
cv2.imshow('origion.jpg',img)
cv2.imshow('translation',tran)  
cv2.imshow('rotation',rota)
cv2.imshow('affine',affi)
cv2.imshow('perspective',pers)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
