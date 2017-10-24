import cv2
import numpy as np
from matplotlib import pyplot as plt
'''
扩充图像边界
• src 输入图像
• top, bottom, left, right 对应边界的像素数目。
• borderType 要添加那种类型的边界,类型如下
– cv2.BORDER_CONSTANT 添加有颜色的常数值边界,还需要
下一个参数(value)。
– cv2.BORDER_REFLECT 边界元素的镜像。比如: fedcba|abcde-
fgh|hgfedcb
– cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT
跟上面一样,但稍作改动。例如: gfedcb|abcdefgh|gfedcba
– cv2.BORDER_REPLICATE 重复最后一个元素。例如: aaaaaa|
abcdefgh|hhhhhhh
– cv2.BORDER_WRAP 不 知 道 怎 么 说 了, 就 像 这 样: cdefgh|
abcdefgh|abcdefg
• value 边界颜色,如果边界的类型是 cv2.BORDER_CONSTANT
'''
BLUE=[255,0,0]
img1=cv2.imread('test.png')
replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()
