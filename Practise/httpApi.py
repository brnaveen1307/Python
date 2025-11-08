import requests

def get_weather(city):
    # Example public API (replace with your own key for real use)
    API_KEY = "your_api_key_here"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    # Construct API URL
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        # Send HTTP GET request
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Convert JSON data to Python dict
        data = response.json()

        # Extract useful info
        city_name = data['name']
        temp = data['main']['temp']
        weather_desc = data['weather'][0]['description']

        print(f"🌤 Weather in {city_name}: {weather_desc.capitalize()}")
        print(f"🌡 Temperature: {temp}°C")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error fetching data: {err}")
    except KeyError:
        print("Invalid city name or response format.")

# Example usage
get_weather("Bangalore")
