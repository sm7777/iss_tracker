import requests
from datetime import datetime, timedelta
import reverse_geocode

def get_response():
    return requests.get('http://api.open-notify.org/iss-now.json').json()

def parse_response(response):
    return [response['timestamp'], response['iss_position']['latitude'], response['iss_position']['longitude']]

def get_location():
    response = parse_response(get_response())
    iss_time = (datetime.utcfromtimestamp(response[0]) - timedelta(hours = 5)).strftime("%I:%M%p " + "CT")
    iss_position = reverse_geocode.search([(float(response[1]), float(response[2]))])

    return [iss_time, iss_position[0]['city'] + ", " + iss_position[0]['country']]