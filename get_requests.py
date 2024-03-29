import requests
import json
import os
from dotenv import load_dotenv


def get_request(path, prms):

    load_dotenv()
    
    response = requests.get(f'{os.getenv("apiUrl")}/{path}', params=prms, headers=json.loads(os.getenv("authKey")))

    return response