import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import os

csv_path = os.path.join("data", "weather.csv")

if not os.path.exists(csv_path):
    print("❌ ERROR: Put a weather dataset CSV inside /data/ as 'weather.csv'")
    exit()

df = pd.read_csv(csv_path)

X = df[['Humidity', 'Pressure (millibars)', 'Apparent Temperature (C)']]
y = df['Temperature (C)']



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

os.makedirs("model", exist_ok=True)
with open("model/weather_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to /model/weather_model.pkl")
