'''
import requests
from geopy.geocoders import Nominatim

res = requests.get('https://ipinfo.io/')
data = res.json()
print (data)
location = data['loc'].split(',')
latitude = location[0]
longitude = location[1]

geolocator = Nominatim(user_agent="geoapiExercises")

location = geolocator.reverse(latitude+","+longitude)
address = location.raw['address']
print(address)

city = address.get('city', '')
state = address.get('state', '')
country = address.get('country', '')
code = address.get('country_code')
zipcode = address.get('postcode')

print('City : ', city)
print('State : ', state)
print('Country : ', country)
print('Zip Code : ', zipcode)
'''

import requests

res = requests.get('https://ipinfo.io/')
data = res.json()


address = data['city'] + ', ' + data['region'] + ', ' + data['country'] + ', Pin-' + data['postal']
print(address)

