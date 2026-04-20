# 📡 IoT Sensor Anomaly Detection using SVM

## 🚀 Project Overview

This project detects anomalies in IoT sensor data using **One-Class SVM**.
It learns normal machine behavior and identifies unusual patterns that may indicate faults or failures.

---

## 🎯 Problem Statement

In industrial environments, machines generate continuous sensor data such as:

* Temperature 🌡️
* Pressure ⚙️
* Vibration 🔊

Detecting abnormal behavior early helps prevent:

* Machine failure
* Production loss
* Maintenance costs

---

## 🧠 Solution

We use **One-Class SVM**, which:

* Trains only on **normal data**
* Learns the pattern of normal operation
* Flags deviations as anomalies 🚨

---

## 🏗️ Architecture

IoT Sensor Data → Preprocessing → Feature Scaling → One-Class SVM → Prediction → Alert

---

## 📁 Project Structure

```
iot-anomaly-svm/
│
├── train.py              # Train the SVM model
├── app.py                # Streamlit real-time app
├── sensor_data.csv       # Dataset
├── model.pkl             # Saved model
├── scaler.pkl            # Scaler
└── requirements.txt      # Dependencies
```

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### 1. Train the model

```bash
python train.py
```

### 2. Run the application

```bash
streamlit run app.py
```

---

## 📊 Input Features

* Temperature
* Pressure
* Vibration

---

## 📌 Output

* ✅ Normal (System working correctly)
* 🚨 Anomaly (Possible fault detected)

---

## 🧪 Example

Input:

```
Temperature: 30
Pressure: 100
Vibration: 0.02
```

Output:

```
✅ System Normal
```

---

## 🔧 Technologies Used

* Python
* Scikit-learn
* Pandas
* NumPy
* Streamlit

---

## 🔥 Future Improvements

* Real-time data streaming
* Dashboard visualization
* Email/SMS alerts
* Model comparison (Isolation Forest, Autoencoders)
* API deployment using FastAPI

---

## 🧠 Key Learning

* Anomaly detection using One-Class SVM
* Feature scaling importance
* Real-time ML application building

---

## 📌 Conclusion

This project demonstrates how machine learning can be used in IoT systems to detect anomalies and prevent failures in real-world industrial environments.

---

