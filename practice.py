import cv2

image = cv2.imread('landscape.jpg')
cv2.imshow('Landscape Image', image)
cv2.waitKey(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Landscape Image', gray_image)
cv2.imwrite('landscape_gray.jpg', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image', hsvImage)
cv2.imwrite('landscape_hsv.jpg', hsvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()



