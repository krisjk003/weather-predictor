from flask import Flask, render_template, request
import pickle
import os
from weather_model import get_live_weather

app = Flask(__name__, template_folder="app/templates")

model_path = os.path.join("model", "weather_model.pkl")
model = None

if os.path.exists(model_path):
    with open(model_path, "rb") as f:
        model = pickle.load(f)
else:
    print("⚠ Model not found. Run train_model.py after adding data.")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    live = None
    city = None

    if request.method == "POST":
        city = request.form.get("city")
        live = get_live_weather(city)

        if model:
            x = [[live['humidity'], live['pressure'], live['feelslike']]]

            prediction = model.predict(x)[0]

    return render_template("index.html", live=live, prediction=prediction, city=city)

if __name__ == "__main__":
    app.run(debug=True)
