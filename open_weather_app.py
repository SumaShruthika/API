import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
CITY = os.getenv('CITY')

URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)

if response.status_code == 200:
    print(f"Fetching weather for city: {CITY}")
    data = response.json()

    weather_info = {
        "city": CITY,
        "temperature": data['main']['temp'],
        "humidity": data['main']['humidity'],
        "weather": data['weather'][0]['main'],
        "wind_speed": data['wind']['speed']
    }

    df = pd.DataFrame([weather_info])
    df.to_csv("weather_data.csv", index=False)
    print("Weather data saved succesfully")

else:
    print(f"Failed to fetch weather data: Error {response.status_code}: {response.text}")