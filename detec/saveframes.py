import os
import pandas as pd
import numpy as np
import cv2
import time

cap = cv2.VideoCapture('cams/new/ByED80IKdIU_06.mp4')
folder_path = "cams/new/frames"

frame_nb = 0

if (cap.isOpened()== False): 
  print("Error opening video stream or file")
while(cap.isOpened()):
    
    ret, frame = cap.read()
    if ret == True:

        if frame_nb == 300:
            cv2.imwrite('frame.png', frame)

        frame_nb = frame_nb + 1

    else: 
        break

print(frame_nb)
cap.release()
cv2.destroyAllWindows()