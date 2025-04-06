# ✈️ Flight Deal Finder

This is an automated Python tool that searches for the cheapest flights from a defined departure city to a list of destination cities. It then updates a Google Sheet with the best price found and optionally sends SMS alerts when a cheaper flight is available than a previously defined threshold.

---

## 📌 Features

- Retrieves destination cities and current lowest prices from a Google Sheet via the Sheety API
- Uses the Amadeus Flight Offers API to search for the best flight deals
- Automatically updates the sheet with the current lowest prices
- Sends SMS alerts via Twilio if a cheaper flight is found
- Uses `.env` for safe environment variable handling

---

## 📁 Project Structure

FlightDealFinder/ ├── data_manager.py # Handles reading from and writing to Google Sheets ├── flight_data.py # Placeholder for future flight data structure ├── flight_search.py # Queries Amadeus API for IATA codes and flight offers ├── main.py # Entry point that runs the whole process ├── notification_manager.py # Placeholder for future notification methods └── README.md # You're here!


---

## 🛠️ Technologies Used

- **Python 3**
- [Amadeus API](https://developers.amadeus.com/) for flight data
- [Sheety API](https://sheety.co/) for Google Sheets interaction
- [Twilio API](https://www.twilio.com/) for SMS notifications
- `.env` for managing environment variables securely
- `requests` for HTTP communication

---

## 🚀 How It Works

1. The program reads a list of cities from a Google Sheet using the Sheety API.
2. For each city:
   - It fetches the corresponding IATA code from Amadeus.
   - It queries available flight prices for the next 6 months.
   - If a new lower price is found, the sheet is updated.
   - If the new price is below the current threshold, an SMS alert is sent.
3. All this happens automatically when running `main.py`.

---

## 🔐 Environment Variables

Create a `.env` file in the root directory with the following keys:

```env
# Amadeus API
AMADEUS_API_KEY=your_amadeus_api_key
AMADEUS_API_SECRET=your_amadeus_api_secret

# Sheety API
SHEETY_ENDPOINT=https://api.sheety.co/your-endpoint/prices
SHEETY_TOKEN=your_sheety_bearer_token

# Twilio API
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth
TWILIO_NUMBER=your_twilio_number
PHONE_NUMBER=your_phone_number

