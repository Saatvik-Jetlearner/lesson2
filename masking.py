import cv2
import numpy as np

foreground = cv2.imread('person_green.jpg')
background = cv2.imread('background.jpg')

background = cv2.resize(background, (foreground.shape[1], foreground.shape[0]))

hsv = cv2.cvtColor(foreground, cv2.COLOR_BGR2HSV)

lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])

mask = cv2.inRange(hsv, lower_green, upper_green)

mask_inv = cv2.bitwise_not(mask)

fg = cv2.bitwise_and(foreground, foreground, mask=mask_inv)
bg = cv2.bitwise_and(background, background, mask=mask)

final_image = cv2.add(fg, bg)

cv2.imshow('Original Image', foreground)
cv2.imshow('White Mask', mask)
cv2.imshow('Final Image', final_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

