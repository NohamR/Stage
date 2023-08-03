import cv2	    # import the OpenCV library
import numpy as np  # import the numpy library
import pyproj
import smopy

global pts_pix,img1
pts_pix = []


def draw_circle(event,x,y,flags,param):
    global pts_pix,img1

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img1, (x, y), 2, (255, 0, 0), -1)
        cv2.imshow("img", img1)
        pts_pix.append([x,y])



img1 = cv2.imread('calibresult2.png',1)

cv2.namedWindow('img')
cv2.setMouseCallback('img', draw_circle)
cv2.imshow('img',img1)
cv2.waitKey(0)

print(pts_pix)