# 📂 Dataset Documentation

This directory documents the dataset used to train the deep learning model for plant disease detection in the AgriVision project.

The dataset consists of crop leaf images collected from a publicly available Kaggle dataset. It contains healthy and diseased leaf images for multiple crop species.

---

# Dataset Source

Platform: Kaggle

Dataset Type:
Plant Disease Image Dataset

Supported Crops

- Banana
- Tomato
- Chilli

---

# Dataset Usage

The dataset was used to train a TensorFlow Convolutional Neural Network (CNN) for disease classification.

Images undergo preprocessing before being passed to the model.

---

# Directory Contents

| File | Description |
|------|-------------|
| Dataset_Details.md | Dataset statistics |
| Dataset_Structure.md | Folder organization |

---

# 📥 Dataset Availability

The original training dataset is **not included** in this repository due to its large size and licensing considerations.

This project was developed using a publicly available **Plant Disease Dataset from Kaggle** for training and evaluation.

Users can download a suitable dataset from Kaggle and organize it according to the directory structure described in **Dataset_Structure.md**.

Once downloaded, the dataset can be arranged as follows:

```text
dataset/
├── train/
│   ├── Banana/
│   ├── Tomato/
│   └── Chilli/
├── valid/
│   ├── Banana/
│   ├── Tomato/
│   └── Chilli/
├── test/
│   ├── Banana/
│   ├── Tomato/
│   └── Chilli/
├── README.md
├── Dataset_Details.md
└── Dataset_Structure.md
```

> **Note:** The dataset folders shown above are provided only as the recommended directory structure and are **not included** in this repository.

