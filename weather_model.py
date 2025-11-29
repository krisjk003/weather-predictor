import requests

API_KEY = "f1f5ea4495894743a3042302252911"

def get_live_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    r = requests.get(url)
    data = r.json()

    return {
        "temp": data["current"]["temp_c"],
        "humidity": data["current"]["humidity"] / 100,   # convert % → fraction
        "feelslike": data["current"]["feelslike_c"],
        "pressure": data["current"]["pressure_mb"]
    }


