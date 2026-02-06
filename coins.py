import cv2
import numpy as np

image = cv2.imread("coins.jpg")

params = cv2.SimpleBlobDetector_Params()

params.filterByCircularity = True
params.minCircularity = 0.9

detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(image)
blank = np.zeros((1, 1))

blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
number_of_blobs = len(keypoints)
text  = "Number of Circular Coins: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)
cv2.imshow("Filtering Circular Coins Only", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()