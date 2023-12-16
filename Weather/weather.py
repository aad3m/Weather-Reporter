import requests

# Can be modified to your own API
API_KEY = '19fc96ed1a1daebe000e661170eff8d6'

city = input('Enter a city name: ')
city = city.title()
# Can be modified to weather program of your liking
base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
weather_data = requests.get(base_url).json()


# Extract specific information
print(f'The weather in {city} currently:')
conditions = weather_data['weather'][0]['description'].title()
current_temp = weather_data['main']['temp']
max_temp = weather_data['main']['temp_max']
min_temp = weather_data['main']['temp_min']
feels_like = weather_data['main']['feels_like']
wind_speed = weather_data['wind']['speed']
visibility = weather_data.get('visibility', 'N/A')

# Print the information
print(f"Conditions: {conditions}")
print(f"Current Temperature: {current_temp} K")
print(f"Today's High: {max_temp} K")
print(f"Today's Low: {min_temp} K")
print(f"Feels Like: {feels_like} K")
print(f"Wind Speed: {wind_speed} m/s")
print(f"Visibility: {visibility} meters")
