import cv2
image =cv2.imread("dog.png")

color = (255, 0, 0)

thickness = 5

line = cv2.line(image, (50, 50), (350, 50), color, thickness)

rectangle = cv2.rectangle(image, (50, 100), (350, 300), color, thickness)

triangle1 = cv2.line(image, (200, 350), (50, 300), color, thickness)
triangle2 = cv2.line(image, (50, 300), (350, 300), color, thickness)
triangle3 = cv2.line(image, (350, 300), (200, 350), color, thickness)


cv2.imshow("Shapes on Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()