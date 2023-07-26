import cv2
import numpy as np
import argparse
import time
import os
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Rectangle, Polygon, Arrow
from matplotlib.lines import Line2D
from matplotlib.collections import EllipseCollection, LineCollection
import sys
from scipy.optimize import least_squares
from scipy.spatial import cKDTree
from imageio import imread
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
from shapely.geometry import Point
import geopandas as gpd
import cartopy
import cartopy.crs as ccrs
import cameratransform as ct
import geodatasets

img = cv2.imread("track/Sylvain/stage_Noham/stage_Noham/image_vide_pts.png")
nh,nw,_ = img.shape
## img : b g r

mask = (img[:,:,0]==0)*(img[:,:,1]==0)*(img[:,:,2]==255)
ind_px_ground_pts = np.where(mask)
px_ground_pts = np.vstack([ind_px_ground_pts[1],ind_px_ground_pts[0]]).T

mask2 = (img[:,:,0]==255)*(img[:,:,1]==0)*(img[:,:,2]==0)
ind_px_ground_pts2 = np.where(mask2)
px_ground_pts2 = np.vstack([ind_px_ground_pts2[1],ind_px_ground_pts2[0]]).T


img_pts = img.copy()
for i,pt in enumerate(px_ground_pts):
    img_pts = cv2.circle(img_pts, pt, 1, (0,0,255), 1)
    txt = str(i)+": "+str(pt)
    img_pts = cv2.putText(img_pts, txt, pt, cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,255,0), 1, cv2.LINE_AA)

distances = np.array([
        [ 0,  8, 37.1],
        [ 1,  7, 10.0],
        [ 2,  4,  6.8],
        [ 2,  5, 28.3],
        [ 2, 10, 17.7],
        [ 2, 12, 19.5],
        [ 3, 11, 20.4],
        [ 4,  7,  3.8],
        [ 5,  9,  9.1],
        [ 5, 13, 12.7],
        [ 6, 11, 11.9],
        [ 9, 10,  7.0],
        [ 9, 13,  9.2],
        [ 9, 15, 16.3],
        [10, 12,  5.3],
        [11, 16, 13.6],
        [14, 20, 16.1],
        [16, 20,  9.7],
        [17, 23, 18.4],
        [17, 25, 16.0],
        [18, 19, 11.6],
        [19, 20, 16.0],
        [19, 24,  8.6],
        [22, 23,  6.0],
        [22, 25,  3.8],
        [23, 24, 12.2]
])
for i,dd in enumerate(distances):
    pt1 = px_ground_pts[int(dd[0]),:]
    pt2 = px_ground_pts[int(dd[1]),:]
    img_pts = cv2.line(img_pts, pt1, pt2, (255,255,0), 2)

# cv2.imwrite("image_vide_pts_labels.png",img_pts)
# cv2.imshow("pts", img_pts)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


## parametres caméra pour initialiser la minimisation de la "cost" fonction
f = 3.2    # en mm
sensor_size = (6.17, 4.55)    # en mm
image_size = (nw,nh)    # en px
elevation = 10 # en m
angle = 45 # inclinaison de la caméra. (0° : caméra orientée vers le bas, 90° : caméra orientée parallèlement au sol, 180° : caméra orientée vers le haut)
heading_deg = 45 # la direction dans laquelle la caméra regarde. (0° : la caméra est orientée « nord », 90° : est, 180° : sud, 270° : ouest)
roll_deg = 0   # rotation de l'image. (0°: camera image is not rotated (landscape format), 90°: camera image is in portrait format, 180°: camera is in upside down landscape format)

## Find camera parameters: [focal,sensorx,sensory,elevation,angle]
def fct_cost(param):
    #print("cost param : ",param)
    f,sx,sy,e,a,b,c = param
    camloc = ct.Camera(
        ct.RectilinearProjection(
            focallength_mm=f,
            sensor=(sx,sy),
            image=image_size
        ),
        ct.SpatialOrientation(
            elevation_m=e,
            tilt_deg=a,
            heading_deg=b,
            roll_deg=c
        )
    )
    pts = []
    for pt in px_ground_pts:
        gpt = camloc.spaceFromImage(pt)
        pts.append(gpt)
    pts = np.array(pts)
    cost = []
    for dd in distances:
        cost.append( np.linalg.norm( pts[int(dd[0]),:]-pts[int(dd[1]),:])-dd[2] )
    
    return np.array(cost)

param = [f, sensor_size[0], sensor_size[1], elevation, angle, heading_deg , roll_deg]
#cost = fct_cost(param)
#print("cost =",cost)

res = least_squares(fct_cost, param)
print(res)


# initialize the camera
cam = ct.Camera(ct.RectilinearProjection(focallength_mm=res.x[0],
                                         sensor=(res.x[1],res.x[2]),
                                         image=image_size),
               ct.SpatialOrientation(elevation_m=res.x[3],
                                     tilt_deg=res.x[4],
                                     heading_deg = res.x[5],
                                     roll_deg = res.x[6] )
                                     )


space_pts = []
for pt in px_ground_pts:
    space_pts.append(cam.spaceFromImage(pt))
space_pts = np.array(space_pts)

space_pts2 = []
for pt in px_ground_pts2:
    space_pts2.append(cam.spaceFromImage(pt))
space_pts2 = np.array(space_pts2)
#print("space_pts2 =", space_pts2)

plt.figure()
plt.scatter(space_pts[:,0], space_pts[:,1], color="red", s=2)
# plt.scatter(space_pts2[:,0], space_pts2[:,1], color="blue", s=1)
plt.plot([28.569, 51.681],[26.665, 89.904], color='blue', linestyle='-', linewidth=1)
for dd in distances:
    plt.plot( [space_pts[int(dd[0]),0], space_pts[int(dd[1]),0]],  [space_pts[int(dd[0]),1], space_pts[int(dd[1]),1]], color="green" )
plt.axis("equal")

plt.show()