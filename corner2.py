import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('lunkuo.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#25指的是找到25个角点；0.01是指：角点的质量水平,0
#到1之间；10指的是最短欧氏距离
corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
# 返回的结果是 [[ 311., 250.]] 两层括号的数组。
corners = np.int0(corners)
for i in corners:
  x,y = i.ravel()
  cv2.circle(img,(x,y),3,255,-1)
  plt.imshow(img),plt.show()
