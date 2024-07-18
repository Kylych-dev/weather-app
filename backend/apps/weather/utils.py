import requests

# Функция для получения координат города
def get_city_coordinates(city):
    print(city)
    url = f"https://nominatim.openstreetmap.org/search"
    params = {
        'q': city,
        'format': 'json',
        'limit': 1
    }
    headers = {
        'User-Agent': 'WeatherApp/1.0'
    }
    response = requests.get(url, params=params, headers=headers)
    print(response)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['lat'], data[0]['lon']
    return None, None