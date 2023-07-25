import cv2
import numpy as np


frame_width = 1280
frame_height = 720
   
size = (frame_width, frame_height)

result = cv2.VideoWriter('deformed.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, size)
    
video_path = 'cams/new/cut2.mp4'
cap = cv2.VideoCapture(video_path)

source_points = np.float32([[129, 379], [658, 332], [251, 551], [916, 445]])

destination_points = np.float32([[200, 350], [800, 350], [200, 600], [800, 600]])

M = cv2.getPerspectiveTransform(source_points, destination_points)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    transformed_frame = cv2.warpPerspective(frame, M, (frame.shape[1], frame.shape[0]))

    # cv2.imshow('Vue de destination', cv2.resize(frame, (1280, 720)))
    
    result.write(cv2.resize(transformed_frame, (1280, 720)))
    cv2.imshow('Vue de destination', cv2.resize(transformed_frame, (1280, 720)))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
result.release()
cv2.destroyAllWindows()
print("The video was successfully saved")