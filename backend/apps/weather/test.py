import unittest
from django.test import Client
from rest_framework import status
from unittest.mock import patch, MagicMock
from apps.weather.views import get_weather  

class WeatherViewTests(unittest.TestCase):
    
    @patch('apps.weather.views.openmeteo_requests.Client')
    @patch('apps.weather.views.get_city_coordinates')
    def test_get_weather_success(self, mock_get_city_coordinates, MockOpenMeteoClient):
        client = Client()
        mock_openmeteo = MockOpenMeteoClient.return_value
        mock_openmeteo.weather_api.return_value = [MagicMock(Hourly=lambda: MagicMock(
            Variables=lambda i: MagicMock(
                ValuesAsNumpy=lambda: 20.0
            )
        ))]
        
        mock_get_city_coordinates.return_value = (40.7128, -74.0060)
        
        response = client.get('/weather/', {'city': 'New York'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('temperature_2m' in response.data[0])
    
    def test_get_weather_missing_city_param(self):
        client = Client()
        response = client.get('/weather/') 
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'City parameter is required.')
    
    @patch('apps.weather.views.get_city_coordinates')
    def test_get_weather_city_not_found(self, mock_get_city_coordinates):
        client = Client()
        mock_get_city_coordinates.return_value = (None, None) 
        
        response = client.get('/weather/', {'city': 'Nonexistent City'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['error'], 'City not found.')

if __name__ == '__main__':
    unittest.main()
