import cv2
import numpy as np

image = cv2.imread("dog.png")

cv2.waitKey(0)
# cv2.destroyAllWindows()


image = cv2.imread("dog.png")

kernel = np.ones((5, 5), np.uint8)
eroded_image = cv2.erode(image, kernel, iterations=1)

cv2.imshow('Eroded Image', eroded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# image = cv2.imread('dog.png')

# blurred = cv2.blur(image, (5, 5))
# cv2.imshow('Blurred Image', blurred)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# image = cv2.imread('dog.png')

# gaussian = cv2.GaussianBlur(image, (5, 5), 0)
# cv2.imshow('Gaussian Blurred Image', gaussian)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# image = cv2.imread('dog.png')

# resized = cv2.resize(image, (300, 300))
# cv2.imshow('Resized Image', resized)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# image = cv2.imread('dog.png')

# border = cv2.copyMakeBorder(
#     image, 20, 20, 20, 20,
#     cv2.BORDER_CONSTANT,
#     value=[0, 0, 255]
# )

# cv2.imshow('Image with Border', border)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Erosion -> Reduces white region, removes noise
# Blurring -> Smoothens the image, reduces detail and noise
# Resizing -> Changes the dimensions of the image
# Borders -> Adds a border around the image
