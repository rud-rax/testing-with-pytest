
import sys
sys.path.append(".")

import requests

from src.mocking.db import phonetic_letters

def get_phonetic_from_db(id):
    return phonetic_letters[id]

def get_users():
    
    response = requests.get(r"https://jsonplaceholder.typicode.com/users")
    
    if response.status_code == 200:
        return response.json()
    
    raise requests.HTTPError