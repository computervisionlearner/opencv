import cv2
import numpy as np
import matplotlib.pylab as plt

'''
特征检测和描述
'''
img = cv2.imread('images/33.jpg')
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
def SIFT(img):
    '''
    第五个参数flags：特征点的绘制模式，其实就是设置特征点的那些信息需要绘制，那些不需要绘制，有以下几种模式可选：
　　DEFAULT：只绘制特征点的坐标点,显示在图像上就是一个个小圆点,每个小圆点的圆心坐标都是特征点的坐标。
　　DRAW_OVER_OUTIMG：函数不创建输出的图像,而是直接在输出图像变量空间绘制,要求本身输出图像变量就 
  是一个初始化好了的,size与type都是已经初始化好的变量
　　NOT_DRAW_SINGLE_POINTS：单点的特征点不被绘制
　　DRAW_RICH_KEYPOINTS：绘制特征点的时候绘制的是一个个带有方向的圆,这种方法同时显示图像的坐 标,size，
  和方向,是最能显示特征的一种绘制方式。
    '''
    sift = cv2.xfeatures2d.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp, des = sift.detectAndCompute(img,None)
    img1 = cv2.drawKeypoints(img,kp,img,flags=4)
    return img1

def SURF(img):
    minHessian = 500
    surf = cv2.xfeatures2d.SURF_create(minHessian)
    
    # find the keypoints and descriptors
    kp, des = surf.detectAndCompute(img,None)
    img1 = cv2.drawKeypoints(img,kp,None,flags=4)
    return img1

def FAST(img):
    fast = cv2.FastFeatureDetector_create()
    kps = fast.detect(img,None)
    img1 = cv2.drawKeypoints(img, kps, None,color=(255,0,0))
    
    return img1

def ORB(img):
    orb = cv2.ORB_create()
    
    # find the keypoints and descriptors
    kps, des = orb.detectAndCompute(img,None)
    img1 = cv2.drawKeypoints(img,kps,None,flags=4)
    return img1
