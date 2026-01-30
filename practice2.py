import cv2

image = cv2.imread('landscape.jpg')

cv2.addWeighted(image, 0.2, image, 0.8, 50, image)
cv2.imshow('Brightened Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
