import requests

class APIClinet:
    def __init__(self, client_id, client_secret, subscriber_code):
        self.client_id = client_id
        self.client_secret = client_secret
        self.subscriber_code = subscriber_code,
        self.api_url = f"https://api.xchange.trimble.com/connect/v1/direct/subscribers/{self.subscriber_code}/vista/ap/2/data/invoices/cache"
        self.headers = {
            "accept": "application/json",
            "X-Application-Key": ""
        }

    def get_data(self):
        response = requests.get(self.api_url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status() # raise an httperror

    def post_data(self, data):
        response = requests.post(self.api_url, headers=self.headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()      
     