import openmeteo_requests, requests_cache
import pandas as pd
from retry_requests import retry
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render

from .utils import get_city_coordinates

cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

@api_view(['GET'])
def get_weather(request):
    city = request.GET.get('city')
    if not city:
        return Response(
            {'error': 'City parameter is required.'}, 
                status=status.HTTP_400_BAD_REQUEST
        )
    

    latitude, longitude = get_city_coordinates(city)
    if latitude is None or longitude is None:
        return Response(
            {'error': 'City not found.'}, 
                status=status.HTTP_404_NOT_FOUND
        )

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m"
    }

    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]

    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy().round(0)

    hourly_data = {
        "date": pd.date_range(
            start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
            end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=hourly.Interval()),
            inclusive="left"
        )
    }
    hourly_data["temperature_2m"] = hourly_temperature_2m

    hourly_dataframe = pd.DataFrame(data=hourly_data)
    current_time = pd.Timestamp.now(tz='UTC')
    next_24_hours = hourly_dataframe[hourly_dataframe['date'] <= current_time + pd.Timedelta(hours=24)]
    weather_data = next_24_hours.to_dict(orient='records')

    return Response(
        weather_data, 
        status=status.HTTP_200_OK
        )

def index(request):
    return render(
        request, 
        'weather/index.html'
        )

  
# def citylist(request):
#     results=City.objects.all
#     return render(request, "weather/index.html",{"showcity":results})
