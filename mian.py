import argparse
from api_client import APIClient

def perform_request(api_client, request_type, post_data=None):
    if request_type == 'get':
        try:
            print("Fetching data")
            response = api_client.get_data()
            print("GET response:")
            print(response)
        except Exception as e:
            print(f"An error occurred during GET request: {e}")
    elif request_type == 'post':
        if post_data is None:
            raise ValueError("POST request requires post_data argument")
        try:
            print("posting data")
            response = api_client.post_data(post_data)
            print("POST response:")
            print(response)
        except Exception as e:
            print(f"An error occurred during POST request: {e}")
    else:
        raise ValueError("Invalid request_type. Use 'get' or 'post'.")
    

def main(client_id, client_secret, subscriber_code, request_type, post_data=None):
    api_client = APIClient(client_id, client_secret, subscriber_code)

    perform_request(api_client, request_type, post_data)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="API Client to interact with Trimble API")
    
    parser.add_argument('--client_id', required=True, help='Client ID')
    parser.add_argument('--client_secret', required=True, help='Client Secret')
    parser.add_argument('--subscriber_code', required=True, help='Subscriber code')
    parser.add_argument('--request_type', required=True, choices=['get', 'post'], help="type of request")
    parser.add_argument('--post_data', type=str, help='post data values')
    
    
    args = parser.parse_args()
    
    
    post_data = None
    
    # call function
    main(args.client_id, args.client_secret, args.subscriber_code, args.request_type, post_data)
