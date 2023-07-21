import numpy as np
import cv2
import time

cap = cv2.VideoCapture('cams/10s.mp4')

# if (cap.isOpened()== False): 
#   print("Error opening video stream or file")
 
# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret == True:
#         cv2.imshow('Frame',frame)
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             break
#     else: 
#         break
  
# cap.release()
# cv2.destroyAllWindows()

while True:
    ret, image = cap.read()    
    # this is the part to add to your code
    cv2.rectangle(image, (0, 0), (200, 200), (0, 0, 0), -1)

    cv2.imshow("My Video", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()