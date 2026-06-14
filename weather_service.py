import requests
from config import API_KEY, BASE_URL


def get_weather_theme(condition_id):

    if 200 <= condition_id <= 232:
        return '\033[94m', "⛈️", "THUNDERSTORM"

    elif 300 <= condition_id <= 531:
        return '\033[94m', "🌧️", "RAINY"

    elif 600 <= condition_id <= 622:
        return '\033[96m', "❄️", "SNOWY"

    elif condition_id == 800:
        return '\033[93m', "☀️", "CLEAR SKY"

    else:
        return '\033[90m', "☁️", "CLOUDY"


def fetch_weather_data(city_name):

    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }

    try:

        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        data = response.json()

        if response.status_code == 200:
            return data, None

        elif response.status_code == 404:
            return None, "City not found."

        elif response.status_code == 401:
            return None, "Invalid API Key."

        else:
            return None, data.get("message", "Unknown error.")

    except requests.exceptions.RequestException:
        return None, "Network connection error."