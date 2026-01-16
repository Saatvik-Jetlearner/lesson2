#Refer - https://www.geeksforgeeks.org/opencv-python-tutorial/

import cv2

image = cv2.imread('dog.png')
cv2.imshow('Dog Image', image)
cv2.waitKey(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Dog Image', gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2

img = cv2.imread('dog.png')
(row, col) = img.shape[:2]

for i in range(row):
    for j in range(col):
        img[i, j] = sum(img[i, j]) * 0.33

cv2.imshow('Grayscale Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
img = cv2.imread("dog.png")
(rows, cols) = img.shape[:2]
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
res = cv2.warpAffine(img, M, (cols, rows))

cv2.imwrite('result.jpg', res)

import cv2
img = cv2.imread('dog.png')

edges = cv2.Canny(img, 100, 200)

cv2.imwrite('result.jpg', edges)


import cv2
img = cv2.imread('dog.png')

hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV Image', hsvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

