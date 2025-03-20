import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

AMADEUS_API_KEY = os.environ["AMADEUS_API_KEY"]
AMADEUS_API_SECRET = os.environ["AMADEUS_API_SECRET"]
BASE_URL = "test.api.amadeus.com/v1"
CREATE_TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
days = 6 * 30
DATES = [(datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(1, days + 1)]
DEPARTURE_CITY = "WRO"

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
}

headers_credentials = {
    "grant_type": "client_credentials",
    "client_id": AMADEUS_API_KEY,
    "client_secret": AMADEUS_API_SECRET,
}

class FlightSearch:
    def __init__(self, name):
        self.cityname = name
        self.token = self.generate_new_token()
        self.auth = {"Authorization": f"Bearer {self.token}"}
        self.iatacode = self.get_iatacode()
        self.best_price = 10000000000000

    @staticmethod
    def generate_new_token():
        token_response = requests.post(url=CREATE_TOKEN_ENDPOINT, headers=headers, data=headers_credentials).json()
        return token_response["access_token"]

    def get_iatacode(self):
        city_response = requests.get(
            url=f"https://test.api.amadeus.com/v1/reference-data/locations/cities?keyword={self.cityname}&max=1",
            headers=self.auth).json()
        return city_response["data"][0]["iataCode"]

    def search_flight(self):
        for date in DATES:
            flight_response = requests.get("https://test.api.amadeus.com/v2/shopping/"
            f"flight-offers?originLocationCode={DEPARTURE_CITY}&destinationLocationCode={self.iatacode}"
            f"&departureDate={date}&adults=1&nonStop=false&max=250", headers=self.auth).json()
            total_price = float(flight_response["data"][0]["price"]["total"])
            if total_price < self.best_price:
                self.best_price = total_price
            return self.best_price
