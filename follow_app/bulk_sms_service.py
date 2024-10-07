import requests

class BulkSMSNigeria:
    def __init__(self, api_token, sender_id):
        self.api_token = api_token
        self.sender_id = sender_id
        self.api_url = "https://www.bulksmsnigeria.com/api/v1/sms/create"

    def send_sms(self, to, message):
        payload = {
            'api_token': self.api_token,
            'from': self.sender_id,
            'to': to,
            'body': message
        }
        response = requests.post(self.api_url, data=payload)
        return response.json()
