import cameratransform as ct
import matplotlib.pyplot as plt

im = plt.imread("gmap.png")
nh,nw,_ = im.shape

# intrinsic camera parameters
f = 6.2    # in mm
sensor_size = (6.17, 4.55)    # in mm
image_size = (nw, nh)    # in px

# initialize the camera
cam = ct.Camera(ct.RectilinearProjection(focallength_mm=f,
                                         sensor=sensor_size,
                                         image=image_size),
               ct.SpatialOrientation(elevation_m=10,
                                     tilt_deg=45))

# display a top view of the image
top_im = cam.getTopViewOfImage(im, [-150, 150, 50, 300], scaling=0.5, do_plot=True)
plt.xlabel("x position in m")
plt.ylabel("y position in m")

plt.show()
