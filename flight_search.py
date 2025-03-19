import requests
from data_manager import DataManager
import os

AMADEUS_API_KEY = os.environ["AMADEUS_API_KEY"]
AMADEUS_API_SECRET = os.environ["AMADEUS_API_SECRET"]
BASE_URL = "test.api.amadeus.com/v1"
CREATE_TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

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
        self.iatacode = self.get_iatacode()
        print(self.token)
        print(self.iatacode)

    @staticmethod
    def generate_new_token():
        token_response = requests.post(url=CREATE_TOKEN_ENDPOINT, headers=headers, data=headers_credentials).json()
        return token_response["access_token"]

    def get_iatacode(self):
        auth = {"Authorization": f"Bearer {self.token}"}
        city_response = requests.get(
            url=f"https://test.api.amadeus.com/v1/reference-data/locations/cities?keyword={self.cityname}&max=1",
            headers=auth).json()
        return city_response["data"][0]["iataCode"]

flight = FlightSearch("Paris")