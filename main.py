from twilio.rest import Client
import requests
from google.cloud import storage
import json
from datetime import datetime

# OpenWeatherMap API credentials
API_KEY = ""

# Location for weather data (Chennai, India)
LATITUDE = 13.0827
LONGITUDE = 80.2707

# Google Cloud Storage bucket
BUCKET_NAME = "weather-alert-data-bucket"

# Twilio API credentials
TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"  # Twilio sandbox WhatsApp number
USER_WHATSAPP_NUMBER = "whatsapp:+"

def fetch_weather_data():
    """Fetch hourly weather data using OpenWeatherMap API."""
    params = {
        "lat": LATITUDE,
        "lon": LONGITUDE,
        "appid": API_KEY,
        "exclude": "current,minutely,daily",
        "units": "metric"
    }
    response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: {response.status_code}, {response.text}")

def upload_to_bucket(data):
    """Upload weather data to Google Cloud Storage."""
    filename = f"weather_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(filename)
    blob.upload_from_string(json.dumps(data), content_type="application/json")
    print(f"Uploaded {filename} to {BUCKET_NAME}.")

def send_whatsapp_message(weather_data):
    """Send hourly weather update via WhatsApp using Twilio."""
    # Extract weather details for the next hour
    next_hour = weather_data['hourly'][0]  # First item is the next hour
    description = next_hour['weather'][0]['description']
    temp = next_hour['temp']
    humidity = next_hour['humidity']

    # Compose WhatsApp message
    message_body = (
        f"Hourly Weather Update for Chennai:\n"
        f"Condition: {description}\n"
        f"Temperature: {temp}°C\n"
        f"Humidity: {humidity}%"
    )

    # Send message using Twilio
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        body=message_body,
        to=USER_WHATSAPP_NUMBER
    )
    print(f"WhatsApp message sent! Message SID: {message.sid}")

def main(event, context):
    """Main entry point for the Cloud Function."""
    print("Triggered weather data ingestion")
    weather_data = fetch_weather_data()
    upload_to_bucket(weather_data)
    send_whatsapp_message(weather_data)
