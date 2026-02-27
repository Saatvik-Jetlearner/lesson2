import cv2
import os

dataset_path = "dataset"
if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

user_id = input("Enter user ID or name: ")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

sample_count = 0
max_samples = 50

print("Starting face detection. Look into the camera...")

while True:

    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        sample_count += 1
        face_img = gray[y:y+h, x:x+w]
        cv2.imwrite(os.path.join(dataset_path, f"{user_id}_{sample_count}.jpg"), face_img)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.putText(frame, f"Sample {sample_count}/{max_samples}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        cv2.imshow('Face Detection', frame)

    if sample_count >= max_samples:
        print("Data collection completed!")
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()