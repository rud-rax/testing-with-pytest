
import sys
sys.path.append(".")

import pytest
import unittest.mock as mock

from src.mocking import service as service


@mock.patch("src.mocking.service.get_phonetic_from_db")
def test_get_phonetic_from_db(mock_get_phonetic_from_db):
    
    mock_get_phonetic_from_db.return_value = 'Mocked Bravo'
    
    phonetic = service.get_phonetic_from_db(2)
    
    assert phonetic == "Mocked Bravo"