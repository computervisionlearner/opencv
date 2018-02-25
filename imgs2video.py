import glob
import cv2

def imgs2video(img_paths,video_name,width,height):
  fourcc = cv2.VideoWriter_fourcc(*'XVID')
  fps = 20
  videowriter = cv2.VideoWriter(video_name,fourcc,fps,(width,height))
  for path in img_paths:
    img = cv2.imread(path)
    videowriter.write(img)
    
  videowriter.release()
  
paths = glob.glob('images/*.png')
paths = sorted(paths, key = lambda x: int(x[7:-4]))

imgs2video(paths,'video.mp4',1080,1920)
