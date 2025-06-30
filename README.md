# VOC_Driver_project
Driver Drowsiness Detection System 🚗💤 A real-time computer vision-based safety tool that detects driver drowsiness using webcam feed, facial landmarks, and Eye Aspect Ratio (EAR). Alerts and logs incidents to help prevent accidents. Built with Python, OpenCV, and MediaPipe.

# 🚗 Driver Drowsiness Detection System

A real-time computer vision-based safety tool that detects driver drowsiness or sleep using facial landmark analysis. It uses Eye Aspect Ratio (EAR) to monitor eye closure and triggers alerts with logging and optional image capture to help prevent accidents.

---

## 📌 Project Description

The Driver Drowsiness Detection System monitors the driver’s eyes via webcam feed using MediaPipe Face Mesh and calculates the Eye Aspect Ratio (EAR) to detect signs of fatigue or sleep. If drowsiness is detected, it logs the incident and optionally captures the frame for review. The system is lightweight and suitable for integration into real-world vehicular safety applications.

---

## 🧠 Key Concepts

- **Facial Landmark Detection** using MediaPipe
- **Eye Aspect Ratio (EAR)** for detecting eye closure
- **Real-time Frame Analysis** using OpenCV
- **Logging** and **Image Saving** for incidents
- **Status Classification**: Active, Drowsy, Sleeping
- **Extensible Audio Alerts** with Pygame (optional)

---

## 🛠️ Technologies Used

- `Python 3`
- `OpenCV`
- `MediaPipe`
- `NumPy`
- `Datetime` and `Logging`
- `Pygame` (optional, for alarm sounds)

---

## 🎯 Features

- 👁️ **EAR Calculation** for both eyes
- 🧠 Differentiates between **Drowsy** and **Sleeping** states
- 📸 Saves screenshots of drowsy/sleep incidents
- 📄 Logs incident data to `drowsiness_log.txt`
- 🛎️ (Optional) Audio alerts using `pygame`
- 🖼️ Displays driver status and EAR in real-time

---

## 🖥️ How to Run

1. Clone the repository:
   ```bash
   git clone 

	2.	Install dependencies:
pip install opencv-python mediapipe numpy pygame

	3.	Run the main script:
python driver_drowsiness.py

Make sure your webcam is connected and accessible by your system.

📂 Project Structure

Driver-Drowsiness-Detection/
│
├── driver_drowsiness.py         # Main script for detection logic
├── drowsiness_log.txt           # Log file (generated after running)
├── incidents/                   # Saved frames of drowsy/sleep events
└── README.md                    # Project documentation

📸 Sample Output
	•	Real-time webcam display showing:
	•	EAR value
	•	Driver Status: Active / Drowsy / Sleeping
	•	Logged and saved images when fatigue is detected

⸻

🙋‍♂️ Author

Sidra Mustafa
Intern @ Vault of Code — June 2025
LinkedIn • GitHub
