import requests

# Replace these with your actual credentials from Termii
TERMII_API_KEY = 'TLDfcyAogBKwuMYnxvPHatThWJqfkOFffeNMTNJaucRjzaoSSeTHugQkzIgDDS'
SENDER_ID = 'JunkeezFoo'
BASE_URL = 'https://api.ng.termii.com/api/sms/send'

def send_sms(to_phone_number, message, bypass_dnd=False):
    url = BASE_URL
    headers = {
        'Content-Type': 'application/json',
    }

    channel = 'dnd' if bypass_dnd else 'generic'
    
    payload = {
        'to': to_phone_number,
        'from': "BSHL",
        'sms': message,
        'type': 'plain',
        'channel': 'generic',
        'api_key': "TLDfcyAogBKwuMYnxvPHatThWJqfkOFffeNMTNJaucRjzaoSSeTHugQkzIgDDS",
        
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()

        # Debug: Print response data
        print(f"Termii API response: {response_data}")

        if response.status_code == 200 and response_data.get('status') == 'success':
            return response_data
        else:
            return {
                "error": f"Failed to send SMS. Status code: {response.status_code}, Response: {response_data}"
            }
    except requests.RequestException as e:
        return {"error": str(e)}
