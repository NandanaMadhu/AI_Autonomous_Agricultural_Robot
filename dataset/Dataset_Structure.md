# 📁 Recommended Dataset Structure

```text
dataset/
├── train/
│   ├── Banana/
│   ├── Tomato/
│   └── Chilli/
│
├── valid/
│   ├── Banana/
│   ├── Tomato/
│   └── Chilli/
│
├── test/
│   ├── Banana/
│   ├── Tomato/
│   └── Chilli/
│
├── README.md
├── Dataset_Details.md
└── Dataset_Structure.md
```

---

## Dataset Split

| Folder | Purpose |
|---------|---------|
| train/ | Model training |
| valid/ | Hyperparameter tuning and validation |
| test/ | Final model evaluation |

---

## Important Note

The original dataset is **not included** in this repository. Users should download a compatible plant disease dataset (e.g., from Kaggle) and organize it using the above directory structure before training the model.
