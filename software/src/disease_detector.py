"""
disease_detector.py

Loads the TensorFlow model and predicts plant diseases.
"""

class DiseaseDetector:

    def __init__(self):
        self.model = None

    def load_model(self):

        print("Loading TensorFlow model...")

        # TODO:
        # Load .keras model

    def predict(self, image):

        print("Running disease prediction...")

        # TODO

        prediction = "Healthy"

        confidence = 98.5

        return prediction, confidence
