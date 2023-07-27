import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
import os
# from imageio import imread
import cameratransform as ct

cap = cv2.VideoCapture('/home/info/Documents/GitHub/Stage/cams/new/cut2.mp4')
folder_path = '/home/info/yolo_tracking/examples/runs/track/exp' + input("Folder path nb") + '/labels/'
name = 'cut2'
fps = 780

allfiles = []
for i in range(1, fps+1):
    allfiles.append(folder_path + name + '_' + str(i) + '.txt')



display_width = 1280
display_height = 720

display_width = 1920
display_height = 1080

width = 1920
height = 1080

frame_nb = 0

bleu = (255, 0, 0)
vert = (0, 255, 0)

a = 2.736
b = -51.49521
x = [i for i in range(-10000, 100000)]
y = [a * xi + b for xi in x]


res = np.array([ 3.99594676,  3.53413555,  4.55      , 16.41739973, 74.96395791, 49.11271189,  2.79384615])
image_size = (width,height) 
cam = ct.Camera(ct.RectilinearProjection(focallength_mm=res[0], sensor=(res[1],res[2]), image=image_size),
               ct.SpatialOrientation(elevation_m=res[3], tilt_deg=res[4], heading_deg = res[5], roll_deg = res[6] ) )


if not cap.isOpened():
    print("Error opening video stream or file")

nbvoituresin = 0
nbvoiturestot = 0

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # print(allfiles[frame_nb])
        df = pd.read_csv(allfiles[frame_nb], header=None, sep=' ')
        px_ground_pts = []
        for index, row in df.iterrows():
            try:
                class_id, center_x, center_y, bbox_width, bbox_height, object_id = row

                center_x = int(center_x * width)
                center_y = int(center_y * height)
                bbox_width = int(bbox_width * width)
                bbox_height = int(bbox_height * height)

                top_left_x = int(center_x - bbox_width / 2)
                top_left_y = int(center_y - bbox_height / 2)
                bottom_right_x = int(center_x + bbox_width / 2)
                bottom_right_y = int(center_y + bbox_height / 2)

                nbvoiturestot += 1

                # (19;112) à (636;714) et (86;86) à (1087;715)
                if (((112-714)/(19-636)) * top_left_x + 112 - ((112-714)/(19-636)) *19 > top_left_y ) and (((86-715)/(86-1097)) * bottom_right_x + 112 - ((86-715)/(86-1097)) *86 < bottom_right_y ):
                    
                    nbvoituresin += 1
            except:
                print('petite erreur de lecture')
                

            else :
                pass

        

        if cv2.waitKey(25) & 0xFF == ord('q'):break
        frame_nb = frame_nb + 1
    else:break

cap.release()
cv2.destroyAllWindows()

print(nbvoituresin)
print(nbvoiturestot)