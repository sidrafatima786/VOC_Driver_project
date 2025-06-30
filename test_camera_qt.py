import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap

class CameraWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Camera Test')
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.resize(640, 480)
        
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Error: Could not open camera")
            sys.exit()
            
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Update every 30ms
        
    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            qt_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(qt_image).scaled(self.size(), Qt.KeepAspectRatio))
            
    def closeEvent(self, event):
        self.cap.release()

if __name__ == '__main__':
    print("Starting Qt camera test...")
    app = QApplication(sys.argv)
    window = CameraWindow()
    window.show()
    print("Window should be visible now")
    sys.exit(app.exec_())
