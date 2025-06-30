import cv2
import numpy as np
import mediapipe as mp
import time
import os
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(filename='drowsiness_log.txt',
                   format='%(asctime)s - %(message)s',
                   level=logging.INFO)

# Configuration parameters
CONFIG = {
    'EYE_AR_THRESH': 0.2,
    'EYE_AR_CONSEC_FRAMES': 6,
    'DROWSY_TIME': 1.0,
    'SLEEP_TIME': 2.0
}

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils

def init_camera():
    print("Initializing camera...")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Could not open camera")
    print("Camera initialized successfully")
    return cap

def compute(ptA, ptB):
    return np.linalg.norm(ptA - ptB)

def eye_aspect_ratio(landmarks, eye_idxs):
    points = []
    for idx in eye_idxs:
        points.append([landmarks[idx].x, landmarks[idx].y])
    points = np.array(points)
    
    A = compute(points[1], points[5])
    B = compute(points[2], points[4])
    C = compute(points[0], points[3])
    ear = (A + B) / (2.0 * C)
    return ear

def save_incident(frame, incident_type):
    if not os.path.exists('incidents'):
        os.makedirs('incidents')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'incidents/{incident_type}_{timestamp}.jpg'
    cv2.imwrite(filename, frame)
    logging.info(f'Incident saved: {filename}')

try:
    print("Starting program...")
    cap = init_camera()
    print("Camera opened, starting main loop...")

    # Initialize variables
    sleep_count = drowsy_count = active_count = 0
    status = "Active"
    color = (0, 255, 0)
    start_time = time.time()

    # MediaPipe eye indices
    LEFT_EYE = [362, 385, 387, 263, 373, 380]
    RIGHT_EYE = [33, 160, 158, 133, 153, 144]

    while True:
        ret, frame = cap.read()
        if not ret:
            logging.error("Failed to grab frame")
            break

        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process the image and detect faces
        results = face_mesh.process(rgb_frame)

        # Convert back to BGR for display
        frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)
        
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # Calculate the eye aspect ratio for both eyes
                left_ear = eye_aspect_ratio(face_landmarks.landmark, LEFT_EYE)
                right_ear = eye_aspect_ratio(face_landmarks.landmark, RIGHT_EYE)
                
                # Average the eye aspect ratio
                ear = (left_ear + right_ear) / 2.0
                
                # Check for drowsiness
                if ear < CONFIG['EYE_AR_THRESH']:
                    sleep_count += 1
                    active_count = 0
                    
                    if sleep_count >= CONFIG['EYE_AR_CONSEC_FRAMES']:
                        elapsed_time = time.time() - start_time
                        if elapsed_time >= CONFIG['SLEEP_TIME']:
                            status = "SLEEPING!"
                            color = (0, 0, 255)
                            save_incident(frame, "sleeping")
                        elif elapsed_time >= CONFIG['DROWSY_TIME']:
                            status = "Drowsy!"
                            color = (0, 165, 255)
                            save_incident(frame, "drowsy")
                else:
                    sleep_count = 0
                    active_count += 1
                    if active_count > CONFIG['EYE_AR_CONSEC_FRAMES']:
                        status = "Active"
                        color = (0, 255, 0)
                        start_time = time.time()
                
                # Draw face mesh
                mp_drawing.draw_landmarks(
                    image=frame,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None
                )
                
                # Display status
                cv2.putText(frame, f"Status: {status}", (10, 30),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
                cv2.putText(frame, f"EAR: {ear:.2f}", (10, 60),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        
        # Display the frame
        cv2.imshow('Driver Drowsiness Detection', frame)
        print(f"Status: {status}, EAR: {ear:.2f}")  # Debug output
        
        # Break loop on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    print("Cleaning up...")
    cap.release()
    cv2.destroyAllWindows()
    print("Program ended.")
