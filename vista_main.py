from vista_client import VistaClient

def main():
    subscriber_code = ""
    url = ""
    application_key = ""

    api_client = VistaClient(subscriber_code, url, application_key)

    response_data = api_client.get_response()

    api_client.save_to_csv(response_data)

if __name__ == "__main__":
    main()

