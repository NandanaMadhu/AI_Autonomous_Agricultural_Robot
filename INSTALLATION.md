# 🚀 Installation Guide

This guide explains how to set up the AgriVision development environment on a Raspberry Pi 4.

---

# Hardware Requirements

- Raspberry Pi 4
- Raspberry Pi Camera Module
- L298N Motor Driver
- Ultrasonic Sensor
- Four DC Gear Motors
- Rechargeable Battery Pack

---

# Software Requirements

- Raspberry Pi OS
- Python 3.10+
- OpenCV
- TensorFlow
- NumPy

---

# Install Python Packages

```bash
pip install opencv-python
pip install tensorflow
pip install numpy
```

---

# Connect Hardware

1. Connect the Raspberry Pi Camera Module to the CSI port.
2. Connect the L298N motor driver to the GPIO pins.
3. Connect the ultrasonic sensor.
4. Power the Raspberry Pi using a regulated power supply.
5. Pair the Raspberry Pi with a Bluetooth-enabled mobile device.

---

# Run the Project

Once the software is configured and the hardware is connected, launch the main application:

```bash
python main.py
```

> **Note:** The original implementation files are not included in this repository. This repository documents the project architecture, hardware design, and software workflow for educational and portfolio purposes.
