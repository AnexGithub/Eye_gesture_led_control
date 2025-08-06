import cv2
import mediapipe as mp
import serial
import time

# Arduino Serial Connection
arduino = serial.Serial('COM20', 9600)  # Change COM port if needed
time.sleep(2)

# MediaPipe Face Mesh setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1)
mp_draw = mp.solutions.drawing_utils

# Eye landmarks (Right Eye)
RIGHT_EYE_TOP = 159
RIGHT_EYE_BOTTOM = 145

# Thresholds
EYE_OPEN_THRESHOLD = 0.025  # Tweak based on lighting/face
prev_command = ""

# Start camera
cap = cv2.VideoCapture(0)

def get_eye_openness(landmarks, image_h, image_w):
    top = landmarks[RIGHT_EYE_TOP]
    bottom = landmarks[RIGHT_EYE_BOTTOM]
    top_y = int(top.y * image_h)
    bottom_y = int(bottom.y * image_h)
    openness = abs(bottom_y - top_y) / image_h
    return openness

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    h, w, _ = frame.shape
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            mp_draw.draw_landmarks(frame, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION)

            eye_open = get_eye_openness(face_landmarks.landmark, h, w)
            command = "ON" if eye_open > EYE_OPEN_THRESHOLD else "OFF"

            # Send only if changed
            if command != prev_command:
                arduino.write((command + '\n').encode())
                print(f"Sent: {command}")
                prev_command = command

            # Show eye openness value
            cv2.putText(frame, f"Eye Openness: {eye_open:.3f}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(frame, f"Relay: {command}", (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    cv2.imshow("Eye-Controlled Relay", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
