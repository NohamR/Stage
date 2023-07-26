import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
import os
# from imageio import imread
import cameratransform as ct

cap = cv2.VideoCapture('cams/new/cut2.mp4')
folder_path = "traitement/delrp/labels/"
name = 'cut2'
fps = 780

allfiles = []
for i in range(1, fps+1):
    allfiles.append(folder_path + name + '_' + str(i) + '.txt')

try:
    os.remove('traitement/distance.txt')
except:
    pass

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

a = 2.736
b = -51.49521
x = [i for i in range(-10000, 100000)]
y = [a * xi + b for xi in x]

# # Cam part
# img = cv2.imread("track/Sylvain/stage_Noham/stage_Noham/image_vide_pts.png")
# nh,nw,_ = img.shape

res = np.array([ 3.99594676,  3.53413555,  4.55      , 16.41739973, 74.96395791, 49.11271189,  2.79384615])
image_size = (width,height) 
cam = ct.Camera(ct.RectilinearProjection(focallength_mm=res[0], sensor=(res[1],res[2]), image=image_size),
               ct.SpatialOrientation(elevation_m=res[3], tilt_deg=res[4], heading_deg = res[5], roll_deg = res[6] ) )


if not cap.isOpened():
    print("Error opening video stream or file")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        df = pd.read_csv(allfiles[frame_nb], header=None, sep=' ')
        px_ground_pts = []
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
                
                label = f'Class: {int(class_id)}, Object ID: {int(object_id)}'
                cv2.putText(frame, label, (top_left_x, top_left_y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, vert, 1)

                # obetnir le centre du rectangle
                center_x = (top_left_x + bottom_right_x) // 2
                center_y = (top_left_y + bottom_right_y) // 2
                cv2.circle(frame, (center_x, center_y), 5, vert, -1)
                
                px_ground_pts += [[center_x, center_y]]
                

            else :
                pass

        # print('px_ground_pts: ', px_ground_pts)
        # print('np.arraypx_ground_pts: ', np.array(px_ground_pts))
         

        space_pts = []
        for pt in np.array(px_ground_pts):
            space_pts.append(cam.spaceFromImage(pt))
        space_pts = np.array(space_pts)

        # print('space_pts: ', space_pts)

        Xb = 26
        Yb = a * Xb + b

        Xv = 1
        Yv = a

        BH = ((space_pts[:,0] - Xb) * Xv) + ((space_pts[:,1] - Yb) * Yv) / np.sqrt( (Xv**2) + (Yv ** 2) )
        # print(BH.tolist())
        with open("traitement/distance_delrp.txt", 'a', encoding='utf-8') as file:
                file.write('\n' + str(BH.tolist()))

        # resized_frame = cv2.resize(frame, (display_width, display_height))
        # cv2.imshow('Frame', resized_frame)
        # plt.figure()

#######################
        # plt.figure(1, figsize=[16, 9])
        # plt.scatter(space_pts[:,0], space_pts[:,1], color="red", s=2)
        # # plt.plot([28.569, 51.681],[26.665, 89.904], color='blue', linestyle='-', linewidth=1)
        
        # plt.plot(x, y, label=f"y = {a}x + {b}", color="black")

        # plt.scatter(Xb, Yb, color="black", s=20)
        # plt.title(frame_nb)
        # plt.legend()

        # # plt.axis("equal")
        # plt.xlim([0, 100])
        # plt.ylim([0, 150])
        # plt.draw()
        # plt.pause(0.0000000000001)
        # plt.clf()
######################

        if cv2.waitKey(25) & 0xFF == ord('q'):break
        frame_nb = frame_nb + 1
    else:break

cap.release()
cv2.destroyAllWindows()