import cv2
import numpy as np

video_source = 'cars.mp4'
cascade_path = 'cars.xml'

cap = cv2.VideoCapture(video_source)

car_cascade = cv2.CascadeClassifier(cascade_path)


if car_cascade.empty():
    print('Error loading cascade classifier')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("End of video stream or cannot read the video.")

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 1, minSize = (30, 30))

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    car_count = len(cars)
    cv2.putText(frame, f'Car Count: {car_count}',
                 (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow('Car Detection', frame)

    if cv2.waitKey(33) == 27:
        break

cap.release()
cv2.destroyAllWindows()