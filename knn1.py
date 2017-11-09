import cv2
import numpy as np
import matplotlib.pylab as plt
import scipy.misc as misc

'''
'''
# Feature set containing (x,y) values of 25 known/training data
x1 = np.random.randint(0,50,(25,2)).astype(np.float32)
y1 = np.zeros((25,1), dtype = np.float32)

x2 = np.random.randint(70,120,(25,2)).astype(np.float32)
y2 = np.ones((25,1), dtype = np.float32) 

trainData = np.concatenate((x1,x2),axis = 0)
# Labels each one either Red or Blue with numbers 0 and 1
responses = np.concatenate((y1,y2),axis = 0)
# Take Red families and plot them
red = trainData[responses.ravel()==0]
plt.scatter(red[:,0],red[:,1],80,'r','^')
# Take Blue families and plot them
blue = trainData[responses.ravel()==1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')

newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')
knn = cv2.ml.KNearest_create()
knn.train(trainData,cv2.ml.ROW_SAMPLE,responses)
ret, results, neighbours ,dist = knn.findNearest(newcomer, 3)

print ("results: ", results,"\n")
print ("neighbours: ", neighbours,"\n")
print ("distances: ", dist)
plt.show()
