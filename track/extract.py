import os
import pandas as pd
import numpy as np
import cv2
import time

cap = cv2.VideoCapture('cams/new/cut2.mp4')
folder_path = "track/expgood/labels/"
name = 'cut2'
fps = 780

allfiles = []
for i in range(1, fps+1):
    allfiles.append(folder_path + name + '_' + str(i) + '.txt')

# Set the desired dimensions for displaying the video
display_width = 1280
display_height = 720

display_width = 1920
display_height = 1080

width = 1920
height = 1080

frame_nb = 0

bleu = (255, 0, 0)
vert = (0, 255, 0)

if not cap.isOpened():
    print("Error opening video stream or file")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
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

            # (19;112) à (636;714) et (86;86) à (1087;715)
            if (((112-714)/(19-636)) * top_left_x + 112 - ((112-714)/(19-636)) *19 > top_left_y ) and (((86-715)/(86-1097)) * bottom_right_x + 112 - ((86-715)/(86-1097)) *86 < bottom_right_y ):
                cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), vert, 2)

                label = f'Class: {int(class_id)}, Object ID: {int(object_id)}'
                cv2.putText(frame, label, (top_left_x, top_left_y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, vert, 1)
            else : 
                cv2.rectangle(frame, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), bleu, 2)

                label = f'Class: {int(class_id)}, Object ID: {int(object_id)}'
                cv2.putText(frame, label, (top_left_x, top_left_y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, bleu, 1)

        resized_frame = cv2.resize(frame, (display_width, display_height))

        cv2.imshow('Frame', resized_frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        frame_nb = frame_nb + 1
    else:
        break

cap.release()
cv2.destroyAllWindows()
