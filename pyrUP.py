import cv2
import numpy as np
DEPTH =3

imgA = cv2.imread('apple.jpg')
imgB = cv2.imread('orange.jpg')
gA=[imgA]
lpA=[]


gB=[imgB]
lpB=[]


for i in range(DEPTH):
  tempA1 = cv2.pyrDown(gA[i])
  tempB1 = cv2.pyrDown(gB[i])
  
  gA.append(tempA1)
  gB.append(tempB1)
  
  lA = cv2.subtract(gA[i] ,cv2.pyrUp(tempA1))
  lB = cv2.subtract(gB[i] ,cv2.pyrUp(tempB1))
  
  lpA.append(lA)
  lpB.append(lB)
lpA.append(gA[-1])
lpB.append(gB[-1])

lpAB = []#将拉布拉斯金字塔的每一层拼接起来
for la,lb in zip(lpA,lpB):
  rows,cols,dpt = la.shape
  ls = np.hstack((la[:,0:cols//2], lb[:,cols//2:]))
  lpAB.append(ls)
  
tempA2 =lpAB[-1]
for i in range(DEPTH,0,-1):
  tempA2 = cv2.pyrUp(tempA2)
  tempA2 = cv2.add(tempA2,lpAB[i-1])
  
cv2.imwrite('apple1.jpg',tempA2)
