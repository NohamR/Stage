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

img = cv2.imread("frame_ground_pts.png")
nh,nw,_ = img.shape
## img : b g r

#mask = (img[:,:,0]==0)*(img[:,:,1]==0)*(img[:,:,2]==255)
#ind_px_ground_pts = np.where(mask)
#px_ground_pts = np.vstack([ind_px_ground_pts[1],ind_px_ground_pts[0]]).T

tab = np.array([
    [215, 257, 41.94076496048223, -85.00154950929712],
    [286, 310, 41.94073282540695, -85.00133550964574],
    [532, 496, 41.94066182925292, -85.00090550095656],
    [359, 462, 41.94064090405561, -85.00098487171928],
    [391, 489, 41.94063193611181, -85.00093564175253],
    [471, 428, 41.940688733067965, -85.00101802659485],
    [536, 433, 41.94069994298754, -85.00099391395807],
    [242, 528, 41.94058410705547, -85.00092057135889],
    [636, 486, 41.9406894803946, -85.00089243994931],
    [243, 552, 41.940578130109905, -85.00088875077661],
    [279, 548, 41.9405866094118, -85.00088875077661],
    [316, 543, 41.940595088712534, -85.00088539801524],
    [347, 540, 41.94060157288293, -85.0008820452539],
    [382, 536, 41.94061055096393, -85.00088070414937],
    [414, 532, 41.94061803269714, -85.00087869249255],
    [447, 526, 41.940624516865206, -85.00087668083574],
    [479, 526, 41.94063449250709, -85.00087198696986],
    [1131, 495, 41.94081056233172, -85.00078883849507],
    [1286, 561, 41.94079011232066, -85.00068557344535],
    [1429, 652, 41.94075918790118, -85.00059236667968],
    [1410, 702, 41.94072826346671, -85.00056554458887],
    [1389, 734, 41.940709309773645, -85.00054811022981],
    [1233, 754, 41.940672399934165, -85.00055816851388],
    [1078, 778, 41.940637485201485, -85.0005668856934],
    [945, 803, 41.94060755827253, -85.00057359121611],
    [1164, 695, 41.94068486947693, -85.00060242496377],
    [892, 556, 41.94070432195875, -85.00075866364288],
    [964, 521, 41.940746219591766, -85.00078816794279],
    [1637, 895, 41.9406788840967, -85.00044752738918],
    [1354, 998, 41.940611049748284, -85.00044819794145],
    [1206, 976, 41.94059758262643, -85.00047233782321],
    [846, 906, 41.94056915202646, -85.00054341636391],
    [944, 999, 41.94056216907017, -85.00049848936177],
    [486, 925, 41.94051977253203, -85.00057962618882],
    [339, 838, 41.94052027131499, -85.00064332865455],
    [98, 826, 41.94048934676464, -85.00068356179082],
    [34, 672, 41.94050630539088, -85.00079621457232],
    [164, 538, 41.94056466298198, -85.00091758453335],
    [131, 593, 41.94054570924032, -85.00086528145621],
    [150, 619, 41.94053872628142, -85.00083108329041],
    [172, 660, 41.94053074575605, -85.00078883849733],
    [1341, 694, 41.940719285401634, -85.00057560287796],
    [1313, 701, 41.94071230246175, -85.00057627343024],
    [1281, 706, 41.940704321958115, -85.00057828508704],
    [1249, 708, 41.94069534389031, -85.00058230840068],
    [265, 379, 41.94066890846167, -85.00116770052296],
    [287, 399, 41.94066092795256, -85.00111807965492]])
px_ground_pts = tab[:,:2].astype(int)

#                                lat                 long
# [216, 258]      [144,172] [41.94076551439789, -85.00155042979091]   65663.889 45130.928  MGRS / UTMREF (WGS84)
# [1287,  561]   [857,372] [41.9407914510061, -85.00068541739631]
# [1354,  999]  [905,668] [41.94061008025459, -85.00044835086464]
# [35,  673]   [25,449]  [41.94050633514897, -85.0007970380291]
#ind_pts = [0, 35, 46, 91]
#px_ground_pts = px_ground_pts[ind_pts,:]

#real_ground_pts = np.array([[41.94076551439789, -85.00155042979091], [41.9407914510061, -85.00068541739631], [41.94061008025459, -85.00044835086464], [41.94050633514897, -85.0007970380291] ])
#real_ground_pts = tab[:,2:]

usa = gpd.read_file(geodatasets.get_path('geoda.natregimes'))
print("usa.crs =",usa.crs)

ax = usa.plot()
ax.set_title("WGS84 (lat/lon)");
# Reproject to Albers contiguous USA
usa = usa.to_crs("ESRI:102003")
ax = usa.plot()
ax.set_title("NAD 1983 Albers contiguous USA");

geometry = gpd.points_from_xy(tab[:,3], tab[:,2]) # long, lat
gts = gpd.GeoDataFrame({"lat": tab[:,2], "lon": tab[:,3]}, geometry=geometry, crs="EPSG:4326")
gts = gts.to_crs("ESRI:102003")
X = gts["geometry"].x
Y = gts["geometry"].y
gts["X"] = X
gts["Y"] = Y
print("gts =",gts.head(10))

real_ground_pts =  gts[["X","Y"]].values

fig, ax = plt.subplots()
usa.plot(ax=ax)
ax.scatter(X,Y,color="red")
ax.set_title("pts coord")
ax.set_xlim([903530.0, 903660.0])
ax.set_ylim([549816.0, 549865.0])

img_pts = img.copy()
for i,pt in enumerate(px_ground_pts):
    img_pts = cv2.circle(img_pts, pt, 1, (0,0,255), 1)
    txt = str(i)+": "+str(pt)
    img_pts = cv2.putText(img_pts, txt, pt, cv2.FONT_HERSHEY_SIMPLEX,
                   0.3, (0,255,0), 1, cv2.LINE_AA)
                   

## parametres caméra pour initialiser la minimisation de la "cost" fonction
f = 3.2    # en mm
sensor_size = (6.17, 4.55)    # en mm
image_size = (nw,nh)    # en px
elevation = 10 # en m
angle = 45 # inclinaison de la caméra. (0° : caméra orientée vers le bas, 90° : caméra orientée parallèlement au sol, 180° : caméra orientée vers le haut)
heading_deg = 45 # la direction dans laquelle la caméra regarde. (0° : la caméra est orientée « nord », 90° : est, 180° : sud, 270° : ouest)
roll_deg = 0   # rotation de l'image. (0°: camera image is not rotated (landscape format), 90°: camera image is in portrait format, 180°: camera is in upside down landscape format)


#px_ground_pts = [ [], [] ]
#ground_pts = [ [], [] ]




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
    #print(pts)
    #print(np.linalg.norm( real_ground_pts-pts[:,:2], axis=1 )**2)
    return np.linalg.norm( real_ground_pts-pts[:,:2], axis=1 )

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
                                     
test_ground_pts = []
for pt in px_ground_pts:
    gpt = cam.spaceFromImage(pt)
    test_ground_pts.append(gpt)
test_ground_pts = np.array(test_ground_pts)
print("test_ground_pts =",test_ground_pts)

plt.figure()
plt.plot(test_ground_pts[:,0], test_ground_pts[:,1],linewidth=0, marker="o")


cv2.imshow("pts", img_pts)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.show()
sys.exit()
