import cv2
image = cv2.imread("dog.png")

color = (255, 255, 0)

color2 = (0, 0, 255)

thickness = 9

line = cv2.line(image, (360, 450), (640, 450), color, thickness)

line2 = cv2.line(image, (500, 310), (500, 590), color2, thickness)

cv2.imshow("Intersecting Lines on Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
