import numpy as np
import cv2

#from video.video_sliders_colors import Yellow_mask

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

# Convierte de RGB a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


#############-- SEMAFORO --#############
# Color Rojo
    lower_red = np.array([161, 155, 84], np.uint8)
    upper_red = np.array([179, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    red = cv2.bitwise_and(frame, frame, mask = red_mask)

# Color Amarillo
    lower_yellow = np.array([25, 50, 50], np.uint8)
    upper_yellow = np.array([32, 255, 255], np.uint8)
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)

# Color Verde
    lower_green = np.array([25, 52, 72], np.uint8)
    upper_green = np.array([102, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    green = cv2.bitwise_and(frame, frame, mask = green_mask)

# Color Azul 
    lower_blue = np.array([94, 80, 2], np.uint8)
    upper_blue = np.array([126, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    blue = cv2.bitwise_and(frame, frame, mask = blue_mask)

# All Colors
    # lower_color = np.array([0, 0, 0], np.uint8)
    # upper_color = np.array([179, 255, 255], np.uint8)
    # color_mask = cv2.inRange(hsv, lower_color, upper_color)
    # colors = cv2.bitwise_and(frame, frame, mask=color_mask)
    # lower_colors_R = np.array([161, 155, 84], np.uint8)
    # upper_colors_R = np.array([179, 255, 255], np.uint8)
    # lower_colors_Y = np.array([25, 50, 50], np.uint8)
    # upper_colors_Y = np.array([32, 255, 255], np.uint8)
    # lower_colors_G = np.array([94, 80, 2], np.uint8)
    # upper_colors_G = np.array([102, 255, 255], np.uint8)
    # Tri_color_mask = (((hsv, lower_colors_R, upper_colors_R) and (hsv, lower_colors_Y, upper_colors_Y) and (hsv, lower_colors_G, upper_colors_G)))
    # tri_color = cv2.bitwise_and(frame, frame, mask = Tri_color_mask)

    cv2.imshow('frame', frame)
    cv2.imshow('Result', green)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
