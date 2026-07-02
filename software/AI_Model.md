# 🧠 AI Model

The AgriVision robot uses a TensorFlow-based Convolutional Neural Network (CNN) to classify plant diseases from crop leaf images.

---

# Model Framework

- TensorFlow
- Python
- OpenCV

---

# Dataset

The model was trained using a publicly available Kaggle Plant Disease Dataset containing images of healthy and diseased leaves.

Supported crops include:

- Banana
- Tomato
- Chilli

---

# Inference Pipeline

1. Capture image
2. Preprocess image
3. Resize input
4. Normalize pixel values
5. Run TensorFlow inference
6. Predict disease class
7. Display prediction
8. Send Bluetooth notification

---

# Future Improvements

- MobileNetV3
- EfficientNet
- YOLO-based disease localization
- Edge TPU acceleration
