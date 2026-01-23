import cv2
image = cv2.imread("dog.png")

start_point = (0, 200)

end_point = (0, 0)

color = (0, 255, 0)

thickness = 9

image = cv2.line(image, start_point, end_point, color, thickness)

start_point = (0, 0)

end_point = (400, 0)

image2 = cv2.line(image, start_point, end_point, color, thickness)

start_point = (0, 200)

end_point = (400, 200)

image3 = cv2.line(image, start_point, end_point, color, thickness)

start_point = (400, 200)

end_point = (400, 0)

image4 = cv2.rectangle(image, start_point, end_point, color, thickness)

start_point = (450, 500)

end_point = (750, 500)

image5 = cv2.line(image, start_point, end_point, color, thickness)

start_point = (200, 400)

end_point = (400, 200)

image6 = cv2.line(image, start_point, end_point, color, thickness)

start_point = (400, 200)

end_point = (600, 400)

image7 = cv2.line(image, start_point, end_point, color, thickness)

start_point = (200, 400)

end_point = (600, 400)

image8 = cv2.line(image, start_point, end_point, color, thickness)




cv2.imshow("Multi Shape Image", image8)
cv2.waitKey(0)
cv2.destroyAllWindows()