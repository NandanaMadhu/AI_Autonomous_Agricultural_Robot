"""
image_processor.py

Preprocesses captured images before AI inference.
"""

import cv2

class ImageProcessor:

    def resize(self, image, size=(224,224)):
        return cv2.resize(image, size)

    def normalize(self, image):
        return image / 255.0

    def preprocess(self, image):

        image = self.resize(image)
        image = self.normalize(image)

        return image
