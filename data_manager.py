import requests
import os
import flight_search
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]
endpoint_name = SHEETY_ENDPOINT.split("/")[-1]

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

class DataManager:
    def __init__(self):
        self.cities = self.get_cities()
        self.update_iata()

    def get_cities(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers).json()
        cities = [city["city"] for city in response[endpoint_name]]
        return cities

    def update_iata(self):
        for i in range(len(self.cities)):
            flight = flight_search.FlightSearch(self.cities[i])
            iata = flight.get_iatacode()
            params = {
                f"price": {
                    "iataCode": f"{iata}"
                }
            }
            endpoint = SHEETY_ENDPOINT + f"/{i + 2}"
            response = requests.put(url=endpoint, json=params, headers=sheety_headers).json()
            print(response)

docs = DataManager()
