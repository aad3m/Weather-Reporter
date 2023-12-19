import requests
print('Welcome to the weather reporter!')

# Get data from openweathermap.org
def get_weather_data(api_key, city):
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}' # website can be changed 
    response = requests.get(base_url)

    # Checks if able to connect to weather data
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
        return None


# convert speed to user-decided unit
def convert_speed(value, unit):
    if unit == 'Miles':
        return value * 2.23694, 'mph'
    elif unit == 'Kilo':
        return value * 3.6, 'km/h'
    else:
        return value, unit

# convert visibility to user-decided unit
def convert_visibility(value, unit):
    if unit == 'Miles':
        value = value * 0.000621371
        unit = 'mi'
    elif unit == 'Kilo':
        value = value * 0.001
        unit = 'km'
    return value, unit


# convert temp to user-decided unit
def convert_temperature(value, unit):
    if unit == 'Fahrenheit':
        return (value - 273.15) * 9 / 5 + 32, 'F'
    elif unit == 'Celsius':
        return value - 273.15, 'C'
    else:
        return value, unit


# diplay all the info
def display_weather_info(city, weather_data, user_units, user_temp):
    degrees_symbol = "\u00b0"

    conditions = weather_data['weather'][0]['description'].title()
    current_temp = weather_data['main']['temp']
    max_temp = weather_data['main']['temp_max']
    min_temp = weather_data['main']['temp_min']
    feels_like = weather_data['main']['feels_like']
    wind_speed = weather_data['wind']['speed']
    visibility = weather_data.get('visibility', 'N/A')

    wind_speed, wind_unit = convert_speed(wind_speed, user_units)
    visibility, visibility_unit = convert_visibility(visibility, user_units)

    current_temp, temp_unit = convert_temperature(current_temp, user_temp)
    max_temp, _ = convert_temperature(max_temp, user_temp)
    min_temp, _ = convert_temperature(min_temp, user_temp)
    feels_like, _ = convert_temperature(feels_like, user_temp)

    print(f'The weather in {city} currently:')
    print(f"Conditions: {conditions}")
    print(f"Current Temperature: {current_temp:.0f} {degrees_symbol}{temp_unit}")
    print(f"Today's High: {max_temp:.0f} {degrees_symbol}{temp_unit}")
    print(f"Today's Low: {min_temp:.0f} {degrees_symbol}{temp_unit}")
    print(f"Feels Like: {feels_like:.0f} {degrees_symbol}{temp_unit}")
    print(f"Wind Speed: {wind_speed:.0f} {wind_unit}")
    print(f"Visibility: {visibility:.0f} {visibility_unit}")


# Running code:
API_KEY = '19fc96ed1a1daebe000e661170eff8d6' # User can you personal API
city = input('Enter a city name: ')
user_units = input('Miles or Kilo: ')
user_units = user_units.title()
user_temp = input('Celsius or Fahrenheit: ')
user_temp = user_temp.title()

weather_data = get_weather_data(API_KEY, city)
if weather_data:
    display_weather_info(city, weather_data, user_units, user_temp)
