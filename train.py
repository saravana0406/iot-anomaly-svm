import pandas as pd
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler
import joblib

# Load data
df = pd.read_csv("sensor_data.csv")

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# Train One-Class SVM
model = OneClassSVM(kernel='rbf', gamma=0.1, nu=0.05)
model.fit(X_scaled)

# Save model
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("✅ Model trained successfully")