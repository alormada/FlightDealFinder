import requests
import os

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]
endpoint_name = SHEETY_ENDPOINT.split("/")[-1]

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

class DataManager:
    def __init__(self):
        self.cities = self.get_cities()

    def get_cities(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers).json()
        cities = [city["city"] for city in response[endpoint_name]]
        return cities

docs = DataManager()