# Driver Drowsiness Detection System

An advanced real-time driver drowsiness detection system using computer vision and deep learning. The system monitors driver's eyes and alerts when signs of drowsiness are detected.

## Features

- Real-time face and eye detection
- Drowsiness and sleep state detection
- Audio alerts for drowsy and sleeping states
- Incident logging and screenshot capture
- Eye Aspect Ratio (EAR) monitoring
- Configurable detection parameters
- Error handling and graceful cleanup

## Requirements

- Python 3.6+
- OpenCV (cv2)
- dlib
- numpy
- imutils
- pygame

Install the required packages using:

```bash
pip install -r requirements.txt
```

You'll also need to download the face landmark predictor file:
- Download [shape_predictor_68_face_landmarks.dat](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
- Extract and place it in the project directory

## Installation

1. Clone this repository
2. Install the required packages
3. Download the face landmark predictor file
4. Add an audio file named `alarm.wav` for alert sounds

## Usage

Run the program:

```bash
python driver_drowsiness.py
```

- Press 'ESC' to exit the program
- The system will automatically create an 'incidents' directory to store screenshots
- A log file 'drowsiness_log.txt' will be created to track all events

## How it Works

The system uses:
1. Face detection to locate the driver's face
2. Facial landmark detection to locate the eyes
3. Eye Aspect Ratio (EAR) calculation to determine eye state
4. Threshold-based detection for drowsiness and sleep states

## Configuration

You can modify the detection parameters in the CONFIG dictionary:
- EYE_AR_THRESH: Threshold for eye aspect ratio
- EYE_AR_CONSEC_FRAMES: Number of consecutive frames for state change
- DROWSY_TIME: Time threshold for drowsy state
- SLEEP_TIME: Time threshold for sleep state

## Contributing

Feel free to submit issues and enhancement requests!
