# utils.py
import requests
from django.conf import settings

def send_whatsapp(phone_number, message):
    url = "https://api.ng.termii.com/api/whatsapp/message/send"
    payload = {
        "to": phone_number,
        "from": settings.TERMII_SENDER_ID,
        "message": message,
        "channel": "whatsapp",
        "api_key": settings.TERMII_API_KEY
    }
    response = requests.post(url, json=payload)
    return response.json()
