import cv2 
import numpy as np

image = cv2.imread('person_green.jpg')

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)

cv2.imshow('Original Image', hsv)
cv2.imshow('Blue Mask', mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
