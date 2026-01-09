import cv2
import numpy as np


image = cv2.imread('dog.png')

if image is None:
    print("Error: Could not read the image.")
    exit()

cv2.imshow('Dog Image', image)

cv2.imwrite('saved_image.png', image)

gray_image = cv2.imread('dog.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Gray Dog Image', gray_image)


blue, green, red = cv2.split(image)
zeros = np.zeros_like(blue)

cv2.imshow('Blue Channel', cv2.merge([blue, zeros, zeros]))
cv2.imshow('Green Channel', cv2.merge([zeros, green, zeros]))
cv2.imshow('Red Channel', cv2.merge([zeros, zeros, red]))

"""

cv2.imread(path) -> Reads an image (default = BGR format)

cv2.imshow(window_name, image) -> Displays an image in a window

cv2.imwrite(filename, image) -> Saves an image to disk

cv2.IMREAD_GRAYSCALE -> Reads the image in grayscale

cv2.split(image) -> Splits the image into Blue, Green, and Red channels

"""

cv2.waitKey(0)
cv2.destroyAllWindows()