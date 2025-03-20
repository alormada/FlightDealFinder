import requests
import os
import flight_search
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]
endpoint_name = SHEETY_ENDPOINT.split("/")[-1]
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
PHONE_NUMBER = os.environ["PHONE_NUMBER"]
TWILIO_NUMBER = os.environ["TWILIO_NUMBER"]

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

class DataManager:
    def __init__(self):
        self.prices = []
        self.cities = self.get_cities()
        self.update_data()

    def get_cities(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers).json()
        print(response)
        cities = [city["city"] for city in response[endpoint_name]]
        self.prices = [city["lowestPrice"] for city in response[endpoint_name]]
        return cities

    def update_data(self):
        for i in range(len(self.cities)):
            flight = flight_search.FlightSearch(self.cities[i])
            iata = flight.iatacode
            try:
                best_price = flight.search_flight()
                try:
                    if best_price < self.prices[i]:
                        message_text = f"Low price alert! Only {best_price} euro to fly from {flight_search.DEPARTURE_CITY} to {iata}."
                        client = Client(account_sid, auth_token)
                        message = client.messages.create(
                            body=message_text,
                            from_=TWILIO_NUMBER,
                            to=PHONE_NUMBER
                        )
                except:
                    pass
            except:
                best_price = "N/A"
            params = {
                f"price": {
                    "iataCode": f"{iata}",
                    "lowestPrice": f"{best_price}"
                }
            }
            endpoint = SHEETY_ENDPOINT + f"/{i + 2}"
            response = requests.put(url=endpoint, json=params, headers=sheety_headers).json()
            print(response)

docs = DataManager()