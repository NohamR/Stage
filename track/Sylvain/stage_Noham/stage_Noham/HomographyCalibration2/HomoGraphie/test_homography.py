import cv2	    # import the OpenCV library
import numpy as np  # import the numpy library
import pyproj
import smopy

# https://www.engineeringtoolbox.com/utm-latitude-longitude-d_1370.html
# http://boulter.com/gps/#48.856676%202.35166

print("On récupère la carte... besoin de réseau !")
# map = Map((lat_min, lon_min, lat_max, lon_max), z=z, tileserver="")
# where the first argument is a box in geographical coordinates, and z
# is the zoom level (from minimum zoom 1 to maximum zoom 19).
map = smopy.Map((48.856421, 2.351325, 48.857103, 2.352135), z=18)
map.save_png("map.png")
print("carte sauvée dans map.png")

WGS84=pyproj.Proj("+init=EPSG:4326")  ## systeme des coord GPS usuelles
UTM31N = pyproj.Proj("+init=EPSG:32631")

# provide points from camera image to map
pts_src = np.array([[  1028,     739], [   184,     377],[   232,     620], [   767,     212]])
pts_dst = np.array([[452419, 5411751], [452478, 5411773],[452441, 5411773], [452475, 5411732]])



pts_pix = np.array([
    [278 , 561],
    [306 , 497],
    [373 , 617],
    [395 , 543],
    [414 , 480],
    [431 , 430],
    [509 , 598],
    [520 , 525],
    [531 , 463],
    [540 , 412],
    [659 , 674],
    [656 , 582],
    [652 , 506],
    [652 , 445],
    [652 , 399],
    [856 , 760],
    [827 , 655],
    [807 , 563],
    [788 , 491],
    [773 , 429],
    [764 , 383],
    [1028 , 738],
    [983 , 627],
    [946 , 544],
    [917 , 476],
    [890 , 418],
    [1211 , 687],
    [1141 , 616],
    [1089 , 528],
    [1049 , 461],
    [1012 , 405],
    [1181 , 606],
    [1282 , 591],
    [1220 , 511],
    [1168 , 449],
    [1125 , 395],
    [1408 , 570],
    [1346 , 497],
    [1283 , 436],
    [1544 , 550],
    [1479 , 483],
    [1415 , 429],
    [1357 , 378],
    [1617 , 466],
    [1553 , 416],
    [1494 , 371],
    [1706 , 461],
    [1726 , 459],
    [1663 , 412],
    [1603 , 370],
    [1548 , 334],
    [1663 , 370],
    [1608 , 336]
    ])


pts_pix = np.array([
[330, 573], [355, 515], [420, 623], [443, 555], [461, 500], [477, 457], [549, 606], [559, 543], [566, 488], [574, 443], [684, 670], [678, 591], [676, 531], [673, 472], [674, 430], [848, 751], [826, 653], [810, 576], [793, 510], [780, 457], [771, 421], [998, 728], [962, 632], [930, 559], [906, 501], [883, 448], [1160, 684], [1097, 618], [1053, 547], [1017, 489], [987, 440], [1130, 611], [1221, 598], [1168, 530], [1120, 478], [1084, 430], [1329, 582], [1274, 519], [1223, 468], [1466, 566], [1398, 506], [1341, 455], [1289, 414], [1540, 491], [1479, 444], [1420, 404],[1630, 470], [1649, 479], [1585, 436], [1524, 400], [1474, 369], [1570, 399], [1516, 368]
   ])
pts_latlon = np.array([
    [48.857062, 2.351683],
    [48.857069, 2.351758],
    [48.857007, 2.351577],
    [48.857035, 2.351653],
    [48.857019, 2.351728],
    [48.856999, 2.351804],
    [48.857004, 2.351549],
    [48.856987, 2.351624],
    [48.856971, 2.351700],
    [48.856950, 2.351774],
    [48.856973, 2.351448],
    [48.856957, 2.351526],
    [48.856936, 2.351600],
    [48.856918, 2.351673],
    [48.856903, 2.351749],
    [48.856940, 2.351351],
    [48.856924, 2.351421],
    [48.856906, 2.351499],
    [48.856887, 2.351579],
    [48.856869, 2.351648],
    [48.856855, 2.351725],
    [48.856895, 2.351325],
    [48.856877, 2.351399],
    [48.856860, 2.351473],
    [48.856843, 2.351548],
    [48.856825, 2.351625],
    [48.856838, 2.351303],
    [48.856830, 2.351374],
    [48.856812, 2.351445],
    [48.856793, 2.351521],
    [48.856775, 2.351597],
    [48.856814, 2.351365],
    [48.856778, 2.351346],
    [48.856762, 2.351420],
    [48.856745, 2.351497],
    [48.856727, 2.351570],
    [48.856732, 2.351316],
    [48.856713, 2.351392],
    [48.856698, 2.351466],
    [48.856667, 2.351285],
    [48.856651, 2.351357],
    [48.856631, 2.351434],
    [48.856614, 2.351505],
    [48.856552, 2.351303],
    [48.856547, 2.351386],
    [48.856531, 2.351463],#
    [48.856506, 2.351277],
    [48.856491, 2.351276],
    [48.856472, 2.351342],
    [48.856455, 2.351420],
    [48.856438, 2.351491],
    [48.856405, 2.351392],
    [48.856388, 2.351467]
    ])

pts_coord = []
for ll in pts_latlon:
    pts_coord.append(pyproj.transform(WGS84, UTM31N, ll[1], ll[0]))
pts_coord = np.array(pts_coord)


# calculate matrix H
h, status = cv2.findHomography(pts_pix, pts_coord)
#h, status = cv2.findHomography(pts_src, pts_dst)  ## Pas assez de points pour être précis
print(h)
#sys.exit()



hm = np.load("/home/mpiidf/TraitementImage/CSRNet-pytorch/heatmap.npz")
hm=hm["hm"]
p=np.where(hm>0.5)

#a=np.concatenate((p[0].reshape((-1,1)),p[1].reshape((-1,1))),axis=1).astype("float32")
#a=np.array([a])


img2 = cv2.imread('map.png',1)
i=0

for ll in pts_latlon:
        xn, yn = map.to_pixels(ll[0], ll[1])
        cv2.circle(img2,(int(np.round(xn)),int(np.round(yn))),2,(0,255,0),-1)

for j in range(0,len(p[0])) :
    temp = np.array([[p[0][j], p[1][j]]], dtype='float32')
    temp = np.array([temp])
    b = cv2.perspectiveTransform(temp, h)
    i=i+1
    lonlat = np.array(pyproj.transform(UTM31N, WGS84, b[0][0][0], b[0][0][1]))
    xn, yn = map.to_pixels(lonlat[1], lonlat[0])
    cv2.circle(img2,(int(np.round(xn)),int(np.round(yn))),2,(0,0,255),-1)
    #if i>1000:
    #    break
    print(i,xn,yn,lonlat)

cv2.imshow('image1',img2)
cv2.waitKey(0)





# mouse callback function
def get_position(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:  #EVENT_MBUTTONDBLCLK: #EVENT_LBUTTONDBLCLK:
        cv2.circle(img1,(x,y),2,(255,0,0),-1)
        a = np.array([[x,  y]], dtype='float32')
        a = np.array([a])


        pt = cv2.perspectiveTransform(a, h)

        # #pt = cam.project_pixel_to_camera_frame(np.array([[x,y]]),distance=-19)
        # #pt3d = cam.project_camera_frame_to_3d(pt)
        # pt3d = cam.project_pixel_to_3d_ray(np.array([[x,y]]), distorted=True, distance=-20.0 )
        lonlat = np.array(pyproj.transform(UTM31N, WGS84, pt[0][0][0], pt[0][0][1]))
        # #test = cam.project_camera_frame_to_3d(np.array([[x,y,0]]))
        # #print("mouse position = (",x,",",y,")"," pt=",pt," pt3d=",pt3d," lonlat=",lonlat )
        # print("mouse position = (",x,",",y,")"," pt3d=",pt3d," lonlat=",lonlat )
        # #print("mouse position = (",x,",",y,")"," test=",test)
        xn, yn = map.to_pixels(lonlat[1], lonlat[0])
        print("mouse position = (",x,",",y,")"," pt = ",pt[0][0]," lonlat=",lonlat)
        # # #print(xn,yn,int(np.round(xn)),int(np.round(yn)))
        cv2.circle(img2,(int(np.round(xn)),int(np.round(yn))),2,(255,0,0),-1)


# Create a black image, a window and bind the function to window
#img = np.zeros((512,512,3), np.uint8)

img1 = cv2.imread('calibresult2.png',1)
img2 = cv2.imread('map.png',1)


#while(1):
#    cv2.imshow('image2',img2)
#    for p in pts_src:
#        cv2.circle(img1,(p[0],p[1]),5,(0,0,255),-1)
#    cv2.imshow('image1',img1)
#    for p in pts_pix:
#        cv2.circle(img1,(p[0],p[1]),5,(0,255,0),-1)
#    for p in pts_dst:
#        lonlat = np.array(pyproj.transform(UTM31N, WGS84, p[0], p[1]))
#        xn, yn = map.to_pixels(lonlat[1], lonlat[0])
#        cv2.circle(img2,(int(np.round(xn)),int(np.round(yn))),2,(0,0,255),-1)
#    for ll in pts_latlon:
#        xn, yn = map.to_pixels(ll[0], ll[1])
#        cv2.circle(img2,(int(np.round(xn)),int(np.round(yn))),2,(0,255,0),-1)


#    cv2.imshow('image1',img1)
#    cv2.setMouseCallback('image1',get_position)
#    if cv2.waitKey(20) & 0xFF == 27:
#        break
#cv2.destroyAllWindows()
