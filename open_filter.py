import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('test2.jpg')
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)#

blur = cv2.GaussianBlur(img,(5,5),0)#

median = cv2.medianBlur(img,5)

#9 邻域直径,两个 75 分别是空间高斯函数标准差,灰度值相似性高斯函数标准差
bila = cv2.bilateralFilter(img,9,75,75)

plt.subplot(231),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(blur),plt.title('gauss')
plt.xticks([]), plt.yticks([])
plt.subplot(234),plt.imshow(median),plt.title('medium')
plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(bila),plt.title('bila')
plt.xticks([]), plt.yticks([])

plt.show()
