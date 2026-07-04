"""
config.py

Central configuration file for the AgriVision system.
"""

# Camera Configuration
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

# Image Processing
IMAGE_SIZE = (224, 224)

# Bluetooth
DEVICE_NAME = "AgriVision"

# Robot Motion
FORWARD_SPEED = 60
TURN_SPEED = 45

# AI Model
MODEL_PATH = "../models/plant_disease_model.keras"

# Obstacle Detection
SAFE_DISTANCE = 30
