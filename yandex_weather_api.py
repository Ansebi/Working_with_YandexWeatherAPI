import os
import requests

YandexWeatherAPI_TOKEN = os.environ.get('YandexWeatherAPI_TOKEN')

"""
lang options are:
«ru_RU» 
«ru_UA»
«uk_UA»
«be_BY»
«kk_KZ»
«tr_TR»
«en_US»
"""

lat = 55.75396
lon = 37.620393
lang = 'en_US'
limit = 7
hours = 'true'
extra = 'true'

request_url = 'https://api.weather.yandex.ru/v2/forecast?'
request_url += f'lat={lat}'
request_url += f'&lon={lon}'
request_url += f'&lang={lang}'  # unnecessary, language_Region combination
request_url += f'&limit={limit}'  # unnecessary, number of days in a forecast with maximum of 7 in the test tariff
request_url += f'&hours={hours}'  # unnecessary, include/exclude hourly data
request_url += f'&extra={extra}'  # unnecessary, include/exclude precipitation details


yandex_response = requests.get(
    request_url,
    headers={'X-Yandex-API-Key': YandexWeatherAPI_TOKEN})

weather_dict = yandex_response.json()
temp_tomorrow_day = weather_dict['forecasts'][1]['parts']['day']['temp_avg']
print(f"The temperature tomorrow is going to be: {temp_tomorrow_day} degrees C")
