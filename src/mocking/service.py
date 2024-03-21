
import sys
sys.path.append(".")

from src.mocking.db import phonetic_letters

def get_phonetic_from_db(id):
    return phonetic_letters[id]

