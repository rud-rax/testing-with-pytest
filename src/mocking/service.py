
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


class Phonetic :
    def __init__(self , value : int) -> None:
        
        self.value = value
        self.phonetic = get_phonetic_from_db(self.value)
        
    def get_phonetic(self) :
        return phonetic_letters[self.value]