#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 09:48:22 2017

@author: fs

https://zhuanlan.zhihu.com/p/31170691?utm_source=wechat_session&utm_medium=social
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
import cv2
import os, sys



def mat2qpixmap(img):
    """ numpy.ndarray to qpixmap
    """
    height, width = img.shape[:2]
    if img.ndim == 3:
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    elif img.ndim ==2:
        #qimage = QImage(img.flatten(), width, height, QImage.Format_Indexed8)
        rgb = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    else:
        raise Exception("Unstatistified image data format!")
    qimage = QImage(rgb.flatten(), width, height, QImage.Format_RGB888)
    qpixmap = QPixmap.fromImage(qimage)
    return qpixmap
    #qlabel.setPixmap(qpixmap)

class ImageView(QWidget):
    """显示 OpenCV 图片的 QWidget 控件
    """
    def __init__(self, winname = "ImageView"):
        super().__init__()
        self.setWindowTitle(winname)
        self.imageLabel = QLabel(self)
        self.imageLabel.setText(winname)
        #self.resize(200,150) # 宽W， 高H
        self.show()

    def setPixmap(self, img):
        #img = cv2.imread("test.png")
        if img is not None:
            H,W = img.shape[:2]
            qpixmap = mat2qpixmap(img)
            self.imageLabel.setPixmap(qpixmap)
            self.resize(W,H) # 宽W， 高H
            self.imageLabel.resize(W,H) # 宽W， 高H

class SliderCanny(QWidget):
    """创建滑动条控制界面，设置Canny边缘检测上下阈值。
    """
    def __init__(self, img=None):
        super().__init__()
        if img is None:
            raise Exception("The Image IS Empty !")
            pass
        self.img = img
        self.gray = cv2.GaussianBlur(cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY), (3,3), 0)
        self.setWindowTitle("Th")
        self.ImageView = ImageView("Source")
        self.CannyView = ImageView("Canny")
        self.ImageView.setPixmap(self.img)
        self.CannyView.setPixmap(self.img)

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        self.addSliders()
        self.show()

    def addSliders(self):
        ## 创建水平滑动条
        self.slider1 = QSlider(Qt.Horizontal)
        self.slider2 = QSlider(Qt.Horizontal)

        ## 设置范围和初值
        self.slider1.setRange(10, 250)
        self.slider2.setRange(10, 250)
        self.slider1.setValue(50)
        self.slider2.setValue(200)

        ## 添加到界面中
        self.mainLayout.addWidget(self.slider1)
        self.mainLayout.addWidget(self.slider2)

        ## 绑定信号槽
        self.slider1.valueChanged.connect(self.doCanny)
        self.slider2.valueChanged.connect(self.doCanny)

    def doCanny(self):
        th1 = self.slider1.value()
        th2 = self.slider2.value()
        print(th1, th2 )
        self.setWindowTitle("TH:{}~{}".format(th1, th2))

        ## Canny 边缘检测
        cannyed = cv2.Canny(self.gray, th1, th2)
        ## 创建彩色边缘
        mask = cannyed > 0                  # 边缘掩模
        canvas = np.zeros_like(self.img)    # 创建画布
        canvas[mask] = img[mask]            # 赋值边缘
        ## 显示结果
        self.CannyView.setPixmap(canvas)

if __name__ == "__main__":
    qApp = QApplication([])
    img = cv2.imread("tangwei.jpeg")
    w2 = SliderCanny(img)
    sys.exit(qApp.exec_())
