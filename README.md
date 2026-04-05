<!-- ===================== BANNER ===================== -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,100:2c5364&height=200&section=header&text=StreamGuard%20🚀&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=35"/>
</p>

<p align="center">
  <b>Real-Time Fraud Detection System using Kafka & Machine Learning</b>
</p>

---

<!-- ===================== BADGES ===================== -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg"/>
  <img src="https://img.shields.io/badge/Apache%20Kafka-Streaming-black"/>
  <img src="https://img.shields.io/badge/ML-Scikit--Learn-orange"/>
  <img src="https://img.shields.io/badge/Status-Active-success"/>
  <img src="https://img.shields.io/badge/License-MIT-green"/>
</p>

---

## 📌 Overview
**StreamGuard** is a real-time fraud detection system built using **Apache Kafka** and **Machine Learning**.

It processes streaming financial transactions and predicts fraud instantly using a trained ML model.

---

## ⚙️ Tech Stack

### Machine Learning & Data Processing
- Python
- Scikit-learn
- Pandas
- Joblib

### Streaming Pipeline
- Apache Kafka

### Utilities
- Logging

---

## 🧠 System Architecture
Producer → Kafka Topic → Consumer → ML Model → Prediction

---

### 🔄 Workflow
- Producer sends transaction data
- Kafka topic (`transactions`) streams data
- Consumer reads incoming messages
- ML model predicts **Fraud / Normal**
- Results are logged in real time

---

## 📁 Project Structure
```text
streamguard-fraud-detection/
├── kafka/
│   ├── producer.py
│   └── consumer.py
├── model/
│   ├── fraud_model.pkl
│   ├── scaler.pkl
│   └── train_model.py
├── .gitignore
└── README.md
```
---

## 🚀 How to Run

### 1️⃣ Start Kafka
Ensure Kafka broker is running locally.

### 2️⃣ Create Kafka Topic
```bash
kafka-topics.bat --create --topic transactions --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

### 3️⃣ Run Consumer (Start First)
```bash
python kafka/consumer.py
```

### 4️⃣ Run Producer
```bash
python kafka/producer.py
```
---

## 📊 Model Details

__- Type:__ Supervised Classification
__- Input:__ Transaction features
__- Output:__
  - 0 → Normal Transaction
  - 1 → Fraudulent Transaction
__- Preprocessing:__ StandardScaler normalization

---

## 📈 Evaluation Metrics
- Precision
- Recall (most critical for fraud detection)
- F1-score
- Accuracy
👉 __Recall is prioritized__ because missing fraud is more costly than false alerts.

---

## ✨ Key Features
- Real-time Kafka streaming pipeline
- Producer–Consumer architecture
- Machine Learning-based fraud detection
- Scalable system design
- Logging & monitoring system
- End-to-end ML pipeline

---

## ⚠️ Important Notes
- Dataset not included due to GitHub size limits
- Dataset used: Kaggle Credit Card Fraud Dataset
- Large files excluded using .gitignore

---

## 👨‍💻 Author
__Tamana__

---

## 🚀 Future Improvements
- Dockerize entire system
- Deploy using AWS MSK Kafka
- Add Streamlit real-time dashboard
- Improve ML model with advanced algorithms

---

<p align="center"> ⭐ If you like this project, consider giving it a star! </p> 

---
