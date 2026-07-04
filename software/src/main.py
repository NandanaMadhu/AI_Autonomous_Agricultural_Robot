"""
AgriVision

Main Application
"""

from camera import Camera
from image_processor import ImageProcessor
from disease_detector import DiseaseDetector
from robot_controller import RobotController
from bluetooth import BluetoothManager
from utils import log

def main():

    log("Starting AgriVision")

    camera = Camera()

    processor = ImageProcessor()

    detector = DiseaseDetector()

    robot = RobotController()

    bluetooth = BluetoothManager()

    detector.load_model()

    robot.move_forward()

    frame = camera.capture_frame()

    if frame is not None:

        image = processor.preprocess(frame)

        disease, confidence = detector.predict(image)

        bluetooth.connect()

        bluetooth.send_prediction(disease)

        bluetooth.disconnect()

        log(f"{disease} detected ({confidence}%)")

    robot.stop()

    camera.release()

if __name__ == "__main__":
    main()
