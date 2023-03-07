import requests

def get_response():
    return requests.get('http://api.open-notify.org/astros.json').json()

def parse_response(response):
    return [tuple(response['people'][index]['name'].split()) 
            for index in range(len(response['people'])) 
            if response['people'][index]['craft'] == 'ISS']

def get_astronaut_names():
    return parse_response(get_response()) 