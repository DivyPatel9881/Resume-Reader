import os

env_var_name = 'CONVERT_API_KEY'

def set_api_key(api_key):
    os.environ[env_var_name] = api_key
    print("Environment variable has been set for your API key.")

def get_api_key():
    return os.getenv(env_var_name)

def clear_api_key():
    os.environ.pop(env_var_name)

def is_api_key_set():
    api_key = get_api_key()
    if api_key == None:
        return False
    else:
        return True