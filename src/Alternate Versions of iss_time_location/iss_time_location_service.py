import requests
from datetime import datetime, timedelta
from geopy.geocoders import Nominatim

def get_response():
    return requests.get('http://api.open-notify.org/iss-now.json').json()

def parse_response(response):
    return [response['timestamp'], response['iss_position']['latitude'], response['iss_position']['longitude']]

def get_location():
    geolocator = Nominatim(user_agent="myGeocoder")
    response = parse_response(get_response())
    iss_time = (datetime.utcfromtimestamp(response[0]) - timedelta(hours = 5)).strftime("%I:%M%p "+"CT")
    iss_position = geolocator.reverse(response[1] + "," + response[2]).raw['address']
    
    return [iss_time, iss_position['city']+ ", " +iss_position['country']]
