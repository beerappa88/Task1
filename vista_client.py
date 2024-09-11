import requests
import pandas as pd 

class VistaClient:
    def __init__(self, subscriber_code, url, application_key):
        self.subscriber_code = subscriber_code
        self.url = url
        self.headers = {
            'x-applicationKey': application_key
        }

    def get_response(self):
        try:
            response = requests.get(self.url, headers=self.headers, params={'subscriber_code': self.subscriber_code})
            response.raise_for_status() 
            return response.json()  

        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the request: {e}")
            return None

    def save_to_csv(self, data, file_name='response_data.csv'):
        if data:
            try:
                if isinstance(data, list):
                    df = pd.DataFrame(data)
                else:
                    df = pd.DataFrame([data])
                df.to_csv(file_name, index=False)
                print(f"Data has been saved to '{file_name}'.")
            except Exception as e:
                print(f"An error occurred while saving data to CSV: {e}")
        else:
            print("No data to save.")



