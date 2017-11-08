
import cv2
import numpy as np
import matplotlib.pylab as plt
import scipy.misc as misc

'''
关于opencv下的kmean算法，函数为cv2.kmeans()
函数的格式为：kmeans(data, K, bestLabels, criteria, attempts, flags)
（1）data: 分类数据，最好是np.float32的数据，每个特征放一列。
之所以是np.float32原因是这种数据类型运算速度快，
同样的数据下如果是uint型数据将会慢死你。
(2) K: 分类数，opencv2的kmeans分类是需要已知分类数的。
(3) bestLabels：预设的分类标签：没有的话 None
(4) criteria：迭代停止的模式选择，这是一个含有三个元素的元组型数。格式为（type,max_iter,epsilon）
其中，type又有两种选择：
        —–cv2.TERM_CRITERIA_EPS :精确度（误差）满足epsilon停止。
        —- cv2.TERM_CRITERIA_MAX_ITER：迭代次数超过max_iter停止。
        —-cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER，两者合体，任意一个满足结束。
（5）attempts：重复试验kmeans算法次数，将会返回最好的一次结果
（6）flags：初始类中心选择，两种方法
cv2.KMEANS_PP_CENTERS ; cv2.KMEANS_RANDOM_CENTERS
'''

X = np.random.randint(25,50,(25,2))
Y = np.random.randint(60,85,(25,2))
Z = np.vstack((X,Y))
# convert to np.float32
Z = np.float32(Z)
# define criteria and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret,label,center=cv2.kmeans(Z,2,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# Now separate the data, Note the flatten()
A = Z[label.ravel()==0]
B = Z[label.ravel()==1]
# Plot the data
plt.scatter(A[:,0],A[:,1])
plt.scatter(B[:,0],B[:,1],c = 'r')
plt.scatter(center[:,0],center[:,1],s = 80,c = 'y', marker = 's')
plt.xlabel('Height'),plt.ylabel('Weight')
plt.show()


img = cv2.imread('tangwei.jpeg')
Z = img.reshape((-1,3))
# convert to np.float32
Z = np.float32(Z)
# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))
cv2.imshow('result1.jpg', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
