import streamlit as st
import joblib
import numpy as np

# Load
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("📡 IoT Sensor Anomaly Detection")

temp = st.number_input("Temperature")
pressure = st.number_input("Pressure")
vibration = st.number_input("Vibration")

if st.button("Check Status"):
    data = np.array([[temp, pressure, vibration]])
    data_scaled = scaler.transform(data)

    pred = model.predict(data_scaled)

    if pred[0] == -1:
        st.error("🚨 Anomaly Detected! Possible Machine Failure")
    else:
        st.success("✅ System Normal")