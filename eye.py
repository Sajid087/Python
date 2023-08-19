import cv2
import numpy as np
import pyautogui

# Initialize webcam capture
cap = cv2.VideoCapture(0)

# Load the Haarcascades for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Main loop
while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) >= 2:
            # Assuming the first two detected eyes are the left and right eyes
            left_eye = eyes[0]
            right_eye = eyes[1]

            # Calculate the center of each eye
            left_eye_center = (x + left_eye[0] + left_eye[2] // 2, y + left_eye[1] + left_eye[3] // 2)
            right_eye_center = (x + right_eye[0] + right_eye[2] // 2, y + right_eye[1] + right_eye[3] // 2)

            # Calculate the midpoint between the two eye centers
            cursor_x = (left_eye_center[0] + right_eye_center[0]) // 2
            cursor_y = (left_eye_center[1] + right_eye_center[1]) // 2

            # Move the mouse cursor
            pyautogui.moveTo(cursor_x, cursor_y, duration=0.1)

    cv2.imshow('Eye Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
