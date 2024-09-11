from vista_client import VistaClient

def read_config(file_path):
    config = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                key, value = line.strip().split('=', 1)  
                config[key] = value
    except Exception as e:
        print(f"An error occurred while reading the configuration file: {e}")
    return config

def main(subscriber_code, url, application_key):
    api_client = VistaClient(subscriber_code, url, application_key)

    response_data = api_client.get_response()

    api_client.save_to_csv(response_data)

if __name__ == "__main__":
    config_file_path = 'config.txt'  
    config = read_config(config_file_path)

   
    if 'subscriber_code' in config and 'url' in config and 'application_key' in config:
        subscriber_code = config['subscriber_code']
        url = config['url']
        application_key = config['application_key']

        main(subscriber_code, url, application_key)
    else:
        print("error the values are not present")
