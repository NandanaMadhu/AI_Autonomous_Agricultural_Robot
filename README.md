<div align="center">

# 🌱 AgriVision

### AI-Powered Autonomous Agricultural Robot for Plant Disease Detection

> *An autonomous four-wheel agricultural robot powered by Raspberry Pi 4, TensorFlow, and OpenCV for real-time plant disease detection and smart crop monitoring.*

<br>

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-FF6F00?style=for-the-badge&logo=tensorflow)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4-C51A4A?style=for-the-badge&logo=raspberrypi)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

</div>

---

# 📑 Table of Contents

- [📖 Project Overview](#-project-overview)
- [🎯 Problem Statement](#-problem-statement)
- [🎯 Objectives](#-objectives)
- [✨ Features](#-features)
- [🏗️ System Architecture](#️-system-architecture)
- [🔩 Hardware Components](#-hardware-components)
- [💻 Software Stack](#-software-stack)
- [⚙️ Project Workflow](#️-project-workflow)
- [📁 Repository Structure](#-repository-structure)
- [🧠 AI Disease Detection Pipeline](#-ai-disease-detection-pipeline)
- [🤖 Autonomous Navigation System](#-autonomous-navigation-system)
- [📡 Bluetooth Communication](#-bluetooth-communication)
- [📊 Results](#-results)
- [🚀 Installation](#-installation)
- [📜 License](#-license)

## 📖 Project Overview

Agriculture plays a vital role in global food production, yet plant diseases continue to cause significant crop losses due to delayed identification and manual inspection. Traditional disease monitoring methods are labor-intensive, time-consuming, and often require expert knowledge, making them unsuitable for large-scale farms.

**AgriVision** is an AI-powered autonomous agricultural robot designed to assist farmers in early plant disease detection. The robot autonomously navigates through crop fields, captures images of plant leaves using a Raspberry Pi Camera Module, processes the images using OpenCV, and classifies diseases with a TensorFlow deep learning model trained on a Kaggle plant disease dataset.

The robot supports disease detection for **banana, chilli, and tomato crops** while simultaneously avoiding obstacles and transmitting detection results wirelessly through the Raspberry Pi's built-in Bluetooth module. By combining robotics, embedded systems, computer vision, and artificial intelligence, the project demonstrates how modern technologies can contribute to precision agriculture and sustainable farming.



## 🎯 Problem Statement

Plant diseases significantly reduce agricultural productivity worldwide. Farmers often rely on manual inspection, which is time-consuming, labor-intensive, and prone to delayed diagnosis. The absence of continuous monitoring makes it difficult to identify diseases during their early stages.

There is a growing need for an intelligent autonomous system capable of continuously monitoring crops, identifying diseases in real time, and assisting farmers in making timely decisions.

This project addresses these challenges by developing an AI-powered autonomous agricultural robot capable of performing real-time disease detection while navigating through crop fields.


## 🎯 Objectives

- Develop an autonomous four-wheel mobile robot for agricultural field monitoring.
- Capture real-time crop images using the Raspberry Pi Camera Module.
- Detect plant diseases using TensorFlow and OpenCV.
- Support disease identification for banana, chilli, and tomato plants.
- Navigate autonomously while avoiding field obstacles.
- Wirelessly transmit disease detection results through Bluetooth.
- Demonstrate the integration of robotics and artificial intelligence for precision agriculture.


## ✨ Features

- 🤖 Autonomous four-wheel robot navigation
- 📷 Real-time image acquisition using Raspberry Pi Camera Module
- 🧠 TensorFlow-based deep learning model for disease classification
- 🌿 Multi-crop disease detection (Banana, Chilli, Tomato)
- 👁 Image preprocessing using OpenCV
- 🚧 Obstacle detection and avoidance
- 📲 Bluetooth-based wireless communication
- 🔋 Battery-powered portable operation
- 🛠 Modular software architecture for future scalability



---

# 🏗️ System Architecture

The AgriVision robot integrates robotics, embedded systems, computer vision, and artificial intelligence into a single autonomous platform. The Raspberry Pi 4 acts as the central controller, coordinating image acquisition, disease detection, autonomous navigation, and wireless communication.

The robot continuously patrols agricultural fields while capturing images of crop leaves using the Raspberry Pi Camera Module. Captured images are preprocessed using OpenCV before being analyzed by a TensorFlow deep learning model trained on a Kaggle plant disease dataset. Based on the prediction results, the robot can notify the user through Bluetooth while continuing its autonomous navigation.

```text
                     Farmer / Mobile Device
                               ▲
                               │
                      Bluetooth Communication
                               ▲
                               │
                    ┌─────────────────────┐
                    │   Raspberry Pi 4    │
                    │ (Main Controller)   │
                    └─────────┬───────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
 Raspberry Pi Camera     Motor Driver        Ultrasonic Sensor
      Module                 │                    │
        │                    ▼                    ▼
        ▼             Four DC Motors      Obstacle Detection
 Image Acquisition
        │
        ▼
 OpenCV Image Processing
        │
        ▼
 TensorFlow Disease Detection
        │
        ▼
 Disease Classification
        │
        ▼
 Bluetooth Notification
```

---


# 🔩 Hardware Components

The robot consists of commercially available hardware components that work together to perform autonomous navigation and AI-based disease detection.

| Component | Description |
|-----------|-------------|
| Raspberry Pi 4 | Main processing unit responsible for robot control and AI inference |
| Raspberry Pi Camera Module | Captures high-resolution images of crop leaves |
| Four DC Gear Motors | Provides robot locomotion |
| Motor Driver Module | Controls motor direction and speed |
| Ultrasonic Sensor | Detects obstacles during navigation |
| Bluetooth (Built-in) | Enables wireless communication with mobile devices |
| Battery Pack | Supplies power to the complete robot |
| Four-Wheel Chassis | Mechanical platform supporting all hardware components |

---

# 💻 Software Stack

The software architecture combines computer vision, artificial intelligence, robotics, and embedded programming to perform autonomous crop monitoring.

| Software | Purpose |
|----------|---------|
| Python | Primary programming language |
| Raspberry Pi OS | Operating System |
| OpenCV | Image acquisition and preprocessing |
| TensorFlow | Plant disease classification |
| NumPy | Numerical computations |
| Git & GitHub | Version control |
| VS Code | Development environment |


---

# ⚙️ Project Workflow

The overall execution of the robot follows the workflow shown below.

```text
Start Robot
     │
     ▼
Initialize Raspberry Pi
     │
     ▼
Initialize Camera
     │
     ▼
Initialize Bluetooth
     │
     ▼
Start Autonomous Navigation
     │
     ▼
Capture Plant Image
     │
     ▼
Image Preprocessing (OpenCV)
     │
     ▼
Disease Prediction (TensorFlow)
     │
     ▼
Healthy Plant?
 ┌───────────────┐
 │               │
 │ YES           │ NO
 │               │
 ▼               ▼
Continue     Display Disease
Navigation       │
                 ▼
        Send Bluetooth Alert
                 │
                 ▼
        Continue Navigation
```







