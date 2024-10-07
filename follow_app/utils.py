import requests
from django.conf import settings

def send_sms(phone_number, message):
    api_key = settings.TERMII_API_KEY
    sender_id = settings.TERMII_SENDER_ID
    url = 'https://api.ng.termii.com/api/sms/send'

    payload = {
        'api_key': api_key,
        'to': phone_number,
        'from': sender_id,
        'sms': message,
        'type': 'plain',
        'channel': 'generic',
    }

    response = requests.post(url, json=payload)
    response_data = response.json()

    if response.status_code == 200 and response_data.get('status') == 'ok':
        return f'Successfully sent SMS to {phone_number}'
    else:
        raise Exception(f'Failed to send SMS: {response_data.get("message", "Unknown error")}')
