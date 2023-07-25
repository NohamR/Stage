import cv2
import numpy as np
import time

image = cv2.imread('frame_pts.png')
img = cv2.imread('frame_pts.png')

def find_red_points(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 254, 254])
    upper_red = np.array([1, 255, 255])
    red_mask = cv2.inRange(hsv_image, lower_red, upper_red)
    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def draw_bounding_boxes(image, contours):
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image


def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        with open("clipboard.txt", 'a', encoding='utf-8') as file:
                file.write('\n' + str(x) + ', ' + str(y))
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 1)
        cv2.imshow('image', img)   
    if event==cv2.EVENT_RBUTTONDOWN:
        pass
  
if __name__=="__main__":
    red_points_contours = find_red_points(image.copy())
    points_list = [tuple(point[0][0]) for point in red_points_contours]
    image_with_boxes = draw_bounding_boxes(image.copy(), red_points_contours)
    display_width = 1920
    display_height = 1080
    resized = cv2.resize(image_with_boxes, (display_width, display_height))

    cv2.imshow("image", image_with_boxes)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# red_points_contours = find_red_points(image.copy())

# points_list = [tuple(point[0][0]) for point in red_points_contours]

# image_with_boxes = draw_bounding_boxes(image.copy(), red_points_contours)

# display_width = 1920
# display_height = 1080

# resized = cv2.resize(image_with_boxes, (display_width, display_height))


# print("Extracted points:", points_list)
# print(len(points_list))
# cv2.imshow("Image avec bordures", image_with_boxes)



cv2.waitKey(0)


cv2.destroyAllWindows()