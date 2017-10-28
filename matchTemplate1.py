import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('tangwei.jpeg',0)

template = cv2.imread('tangweiface.jpeg',0)
w, h = template.shape[::-1]
# All the 6 methods for comparison in a list
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
for meth in methods:
  fig, ax = plt.subplots(figsize=(12, 12))
  img2 = img.copy()
  #exec 语句用来执行储存在字符串或文件中的 Python 语句。
  # 例如,我们可以在运行时生成一个包含 Python 代码的字符串,然后使用 exec 语句执行这些语句。
  #eval 语句用来计算存储在字符串中的有效 Python 表达式
  method = eval(meth)
  # Apply template Matching
  res = cv2.matchTemplate(img2,template,method)
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)#return (x,y)
  # 使用不同的比较方法,对结果的解释不同
  # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
  if meth in ['cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']:
    top_left = min_loc
  else:
    top_left = max_loc
  bottom_right = (top_left[0] + w, top_left[1] + h)
  cv2.rectangle(img2,top_left, bottom_right, 255, 2)
  plt.subplot(121),plt.imshow(res,cmap = 'gray')
  plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
  
  plt.subplot(122),plt.imshow(img2,cmap = 'gray')
  plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
  plt.suptitle(meth)
  plt.show()
