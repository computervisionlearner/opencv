#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:36:36 2017

@author: fs
"""
import cv2

def camera(file, SaveVideo):
    camera = cv2.VideoCapture(file)

    cv2.namedWindow('', 0)
    _, frame = camera.read()
    height, width, _ = frame.shape
    cv2.resizeWindow('', width, height)
    
    if SaveVideo:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')

        videoWriter = cv2.VideoWriter('video.avi', fourcc, 20, (width, height))

    while camera.isOpened():
        ret, frame = camera.read()
        if ret is not True:
            print ('\nEnd of Video')
            break

        if SaveVideo:
            frame1 = cv2.flip(frame,0)
            
            videoWriter.write(frame1)
        cv2.imshow('', frame)

        choice = cv2.waitKey(1)&0xFF
        
        if choice == ord('q'): break

    if SaveVideo:
        videoWriter.release()
    camera.release()
    cv2.destroyAllWindows()
    
    
    
camera('test.mp4',True)
