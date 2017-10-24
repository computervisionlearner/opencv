import cv2
events=[i for i in dir(cv2) if 'EVENT'in i]
print( events )#查看所有的鼠标事件

'''

    CV_EVENT_MOUSEMOVE      =0,   //鼠标移动
    CV_EVENT_LBUTTONDOWN    =1,   //按下左键
    CV_EVENT_RBUTTONDOWN    =2,   //按下右键
    CV_EVENT_MBUTTONDOWN    =3,   //按下中键
    CV_EVENT_LBUTTONUP      =4,   //放开左键
    CV_EVENT_RBUTTONUP      =5,   //放开右键
    CV_EVENT_MBUTTONUP      =6,   //放开中键
    CV_EVENT_LBUTTONDBLCLK  =7,   //左键双击
    CV_EVENT_RBUTTONDBLCLK  =8,   //右键双击
    CV_EVENT_MBUTTONDBLCLK  =9,   //中键双击
    CV_EVENT_MOUSEWHEEL     =10,  //滚轮滚动
    CV_EVENT_MOUSEHWHEEL    =11   //横向滚轮滚动
    CV_EVENT_FLAG_LBUTTON   =1,   //左键拖拽
    CV_EVENT_FLAG_RBUTTON   =2,   //右键拖拽
    CV_EVENT_FLAG_MBUTTON   =4,   //中键拖拽
    CV_EVENT_FLAG_CTRLKEY   =8,   //按住CTRL拖拽
    CV_EVENT_FLAG_SHIFTKEY  =16,  //按住Shift拖拽
    CV_EVENT_FLAG_ALTKEY    =32   //按住ALT拖拽

'''
import cv2
import numpy as np

# 当鼠标按下时变为 True
drawing=False
# 如果 mode 为 true 绘制矩形。按下 'm' 变成绘制曲线。
mode=True
ix,iy=-1,-1
# 创建回调函数
def draw_circle(event,x,y,flags,param):
  global ix,iy,drawing,mode
  # 当按下左键是返回起始位置坐标
  if event==cv2.EVENT_LBUTTONDOWN:
    drawing=True
    ix,iy=x,y
  # 当鼠标左键按下并移动是绘制图形。 event 可以查看移动, flag 查看是否按下
  elif event==cv2.EVENT_MOUSEMOVE and flags==33:
    if drawing==True:
      if mode==True:
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
      else:
        # 绘制圆圈,小圆点连在一起就成了线, 3 代表了笔画的粗细
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        # 下面注释掉的代码是起始点为圆心,起点到终点为半径的
        # r=int(np.sqrt((x-ix)**2+(y-iy)**2))
        # cv2.circle(img,(x,y),r,(0,0,255),-1)
  # 当鼠标松开停止绘画。
  elif event==cv2.EVENT_LBUTTONUP:
    drawing==False
    #if mode==True:
      #cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
    #else:
      #cv2.circle(img,(x,y),5,(0,0,255),-1)
      
      
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
  cv2.imshow('image',img)
  k=cv2.waitKey(1)&0xFF
  if k==ord('m'):
    mode=not mode
  elif k==27:
    break
  
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
cv2.waitKey(1)
