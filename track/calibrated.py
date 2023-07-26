import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
from imageio import imread
import cameratransform as ct

img = cv2.imread("track/Sylvain/stage_Noham/stage_Noham/image_vide_pts.png")
nh,nw,_ = img.shape

res = np.array([ 3.99594676,  3.53413555,  4.55      , 16.41739973, 74.96395791, 49.11271189,  2.79384615])
image_size = (nw,nh) 
cam = ct.Camera(ct.RectilinearProjection(focallength_mm=res[0], sensor=(res[1],res[2]), image=image_size),
               ct.SpatialOrientation(elevation_m=res[3], tilt_deg=res[4], heading_deg = res[5], roll_deg = res[6] ) )


mask = (img[:,:,0]==0)*(img[:,:,1]==0)*(img[:,:,2]==255)
ind_px_ground_pts = np.where(mask)
print('ind_px_ground_pts: ', ind_px_ground_pts)
px_ground_pts = np.vstack([ind_px_ground_pts[1],ind_px_ground_pts[0]]).T
print(px_ground_pts)



space_pts = []
for pt in px_ground_pts:
    space_pts.append(cam.spaceFromImage(pt))
space_pts = np.array(space_pts)


plt.figure()
plt.scatter(space_pts[:,0], space_pts[:,1], color="red", s=2)
plt.axis("equal")

plt.draw()
plt.pause(1)