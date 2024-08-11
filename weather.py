
import requests

def get_weather_data(api_key, location):
    # Define the API endpoint
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    
    # Send a request to the API
    response = requests.get(url)
    
    # Check if the response was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def parse_weather_data(data):
    # Extract relevant information from the response
    city = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"].capitalize()
    
    return {
        "city": city,
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "description": description
    }

def display_weather_info(weather_info):
    # Display the weather information in a user-friendly format
    print(f"Weather in {weather_info['city']}:")
    print(f"Temperature: {weather_info['temperature']}°C")
    print(f"Humidity: {weather_info['humidity']}:")
    print(f"Wind Speed: {weather_info['wind_speed']}km/ph")
    print(f"Description: {weather_info['description']}:")

