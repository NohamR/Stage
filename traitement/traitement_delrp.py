import pandas as pd
import numpy as np
import cv2

folder_path = "traitement/delrp/labels/"
name = 'cut2'
newname = 'post_' + name

fps = 780
# fps = 3

allfiles = []
for i in range(1, fps+1):
    allfiles.append(folder_path + name + '_' + str(i) + '.txt')

def run():
    frame_nb = 0
    for i in range(fps-2):
        for i in range(0,3):
            # print(allfiles[frame_nb+i])
            pass
        df1 = pd.read_csv(allfiles[frame_nb], header=None, sep=' ')
        df2 = pd.read_csv(allfiles[frame_nb+1], header=None, sep=' ')
        df3 = pd.read_csv(allfiles[frame_nb+2], header=None, sep=' ')

        od_1 = []
        od_2 = []
        od_3 = []

        for index, row in df1.iterrows():
            class_id_1, center_x_1, center_y_1, bbox_width_1, bbox_height_1, object_id_1 = row
            od_1.append(int(object_id_1))

        for index, row in df2.iterrows():
            class_id_2, center_x_2, center_y_2, bbox_width_2, bbox_height_2, object_id_2 = row
            od_2.append(int(object_id_2))

        for index, row in df3.iterrows():
            class_id_3, center_x_3, center_y_3, bbox_width_3, bbox_height_3, object_id_3 = row
            od_3.append(int(object_id_3))

        numeros_communs = list(set(od_1) & set(od_3))
        # print('numeros_communs: ', numeros_communs)

        numeros_diff = list(set(numeros_communs) - set(od_2))
        # print('numeros_diff: ', numeros_diff)

        if len(numeros_diff) > 0:
            df2 = df3
            df2.to_csv(allfiles[frame_nb+1], header=None, index=False, sep=' ')


        frame_nb = frame_nb + 1


run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()
run()