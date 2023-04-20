import requests

# OpenWeatherMap API key
API_key = '...'

# City code for skelleftea, Sweden
city_code = '602913'

# API endpoint for current weather data by city code
url = f'http://api.openweathermap.org/data/2.5/forecast?id={city_code}&appid={API_key}&units=metric'

# Send an HTTP request to the API endpoint and get the response
response = requests.get(url)

# Convert the JSON response to a Python object
data = response.json()
#print(data)
# Display the weather data
print("City:", data['city']['name'])
print("Temperature:", data['list'][0]['main']['temp'])
print("Humidity:", data['list'][0]['main']['humidity'])
print("Weather:", data['list'][0]['weather'][0]['main'])
