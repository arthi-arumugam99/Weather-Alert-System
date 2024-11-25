# Weather Alert System

## **Project Overview**
The **Automated Weather Alert System** is a cloud-based project that provides hourly weather updates for Chennai, stores them in Google Cloud Storage, and sends real-time WhatsApp notifications to users. The system is designed to be fully automated, scalable, and reliable, ensuring users stay informed about the latest weather conditions.


## **Technologies Used**
- Python
- Google Cloud Scheduler
- Google Pub/Sub
- Google Cloud Functions
- Google Cloud Storage
- OpenWeatherMap API (for weather data)
- Twilio API (for WhatsApp notifications)


## **Data Architecture**
1. **Trigger Mechanism**: A **Cloud Scheduler** triggers the system every hour.
2. **Event Queue**: A **Pub/Sub topic** (`weather-ingestion`) manages events and triggers the Cloud Function.
3. **Data Processing**: The **Cloud Function**:
   - Fetches weather data from the **OpenWeatherMap API**.
   - Stores the weather data as JSON files in **Google Cloud Storage**.
   - Sends a WhatsApp notification with weather updates using the **Twilio API**.
4. **Data Storage**: JSON files are archived in **Google Cloud Storage** for future analysis or monitoring.

![diagram-export-25-11-2024-11_19_25](https://github.com/user-attachments/assets/c6377a4f-8162-4023-9473-226c7e6b4cc6)


## **Project Objectives**
1. Automate the process of fetching hourly weather updates for Chennai.
2. Store fetched data in a scalable and accessible storage system.
3. Notify users in real-time about weather updates via WhatsApp.
4. Provide a reliable and scalable architecture using cloud-native tools.



## **Project Flow**
1. **Cloud Scheduler** triggers a Pub/Sub topic every hour.
2. **Pub/Sub** forwards the message to the **Cloud Function**.
3. **Cloud Function** performs the following tasks:
   - Fetches weather data using the OpenWeatherMap API.
   - Saves the fetched data to Google Cloud Storage in JSON format.
   - Sends a WhatsApp message to the user using the Twilio API, detailing:
     - Weather condition
     - Temperature
     - Humidity
4. Results are stored in the cloud and delivered in real-time to the user.


## **Results**
- The system successfully fetches and stores weather updates hourly.
- Real-time WhatsApp notifications provide users with timely weather alerts.
- JSON data is archived in Google Cloud Storage for potential analysis or reporting.

  ![69796](https://github.com/user-attachments/assets/e47335c5-8c1d-4a49-bb8d-356d76510586)


## **Challenges Faced**
1. **Integration Issues**:
   - Initial setup of Twilio WhatsApp Sandbox for testing required careful configuration.
2. **API Rate Limits**:
   - OpenWeatherMap API rate limits needed handling to ensure consistent data fetching.
3. **Error Handling**:
   - Managing intermittent network failures while fetching weather data.
