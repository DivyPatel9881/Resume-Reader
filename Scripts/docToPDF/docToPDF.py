import convertapi

from APIKey import *

if is_api_key_set():
    convertapi.api_secret = get_api_key()
else:
    print("Enter your API key to make conversions.")
    api_key = input()
    set_api_key(api_key)
    convertapi.api_secret = api_key

print("Found your API endpoint.")

