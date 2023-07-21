import os
import pandas as pd
import numpy as np
import cv2
import time

cap = cv2.VideoCapture('cams/10s.mp4')
folder_path = "track/exp2/labels/"
name = '10s'
fps = 141

allfiles = []
for i in range(1,fps+1):
    allfiles.append(folder_path + name + '_' + str(i) + '.txt')

width = 480
height = 360

frame_nb = 0

if (cap.isOpened()== False): 
  print("Error opening video stream or file")
while(cap.isOpened()):
    
    ret, frame = cap.read()
    if ret == True:

        df = pd.read_csv(allfiles[frame_nb], header=None, sep=' ')
        
        for index, row in df.iterrows():
            class_id, center_x, center_y, bbox_width, bbox_height, object_id = row

            center_x = int(center_x * width)
            center_y = int(center_y * height)
            bbox_width = int(bbox_width * width)
            bbox_height = int(bbox_height * height)

            top_left_x = int(center_x - bbox_width / 2)
            top_left_y = int(center_y - bbox_height / 2)
            bottom_right_x = int(center_x + bbox_width / 2)
            bottom_right_y = int(center_y + bbox_height / 2)

            cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (255, 0, 0), 2)
            
            label = f'Class: {int(class_id)}, Object ID: {int(object_id)}'
            cv2.putText(frame, label, (top_left_x, top_left_y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

        cv2.imshow('Frame',frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        frame_nb = frame_nb + 1

    else: 
        break
cap.release()
cv2.destroyAllWindows()