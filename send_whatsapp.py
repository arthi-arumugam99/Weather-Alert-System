from twilio.rest import Client

# Twilio API credentials
account_sid = 'AC53f642d38652002ed88162b8378bee60'
auth_token = '4e3fd4ce29b03064ffdef7dbd174f4f8'
twilio_whatsapp_number = 'whatsapp:+14155238886'  # Twilio sandbox WhatsApp number
recipient_whatsapp_number = 'whatsapp:+919677667794'  # Replace with your WhatsApp number in E.164 format (e.g., whatsapp:+14155552671)

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Compose and send the WhatsApp message
message = client.messages.create(
    from_=twilio_whatsapp_number,
    body="Hello! This is a test message sent via Twilio WhatsApp API.",
    to=recipient_whatsapp_number
)

print(f"Message sent successfully! Message SID: {message.sid}")
