"""
camera.py

Handles image acquisition using the Raspberry Pi Camera Module.
"""

import cv2

class Camera:

    def __init__(self):
        self.camera = cv2.VideoCapture(0)

    def capture_frame(self):
        success, frame = self.camera.read()

        if success:
            return frame

        return None

    def release(self):
        self.camera.release()
