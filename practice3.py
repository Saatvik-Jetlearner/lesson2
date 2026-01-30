import cv2

image = cv2.imread('landscape.jpg')
image2 = cv2.imread('landscape_gray.jpg')
cv2.imshow('Image 1', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('Image 2', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

subtracted_image = cv2.subtract(image, image2)
cv2.imshow('Subtracted Image', subtracted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
