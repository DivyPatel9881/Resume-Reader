import os

def set_api_key(api_key):
    os.environ['CONVERT_API_KEY'] = api_key
    print("Environment variable has been set for your API key.")

def get_api_key():
    return os.getenv('CONVERT_API_KEY')

def is_api_key_set():
    api_key = get_api_key()
    if api_key == None:
        return False
    else:
        return True