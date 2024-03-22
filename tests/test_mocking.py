
import sys
sys.path.append(".")

import pytest
import unittest.mock as mock

import requests

from src.mocking import service as service


@mock.patch("src.mocking.service.get_phonetic_from_db")
def test_get_phonetic_from_db(mock_get_phonetic_from_db):
    
    mock_get_phonetic_from_db.return_value = 'Mocked Bravo'
    
    phonetic = service.get_phonetic_from_db(2)
    
    assert phonetic == "Mocked Bravo"
    

@mock.patch("requests.get")
def test_get_users(mock_get):
    
    mock_response = mock.Mock()
    mock_response.status_code = 200 
    mock_response.json.return_value = {"id" : 8888 , "name" : "Bill"}
    
    mock_get.return_value = mock_response
    
    data = service.get_users()
    
    assert data == {"id" : 8888 , "name" : "Bill"}
    
    
@mock.patch("requests.get")
def test_get_users_error(mock_get):
    
    mock_response = mock.Mock()
    mock_response.status_code = 400
    
    mock_get.return_value = mock_response
    
    with pytest.raises(requests.HTTPError) :
        service.get_users()
        
        
def test_spy_method(mocker):
    class Foo(object):
        def bar(self, v):
            return v * 2

    foo = Foo()
    spy = mocker.spy(foo, 'bar')
    assert foo.bar(21) == 42

    spy.assert_called_once_with(21)
    assert spy.spy_return == 42



def test_spy_function(mocker):

    spy = mocker.spy(service, "get_phonetic_from_db")
    
    
    
    assert service.get_phonetic_from_db(1) == "Alpha"
    assert service.get_phonetic_from_db(2) == "Bravo"
    assert service.get_phonetic_from_db(3) == "Charlie"
    
    assert spy.call_count == 3
    assert spy.spy_return == "Charlie"
    

# def test_get_users_error2(mocker):
    
#     spy = mocker.spy(service , "requests.get")
    
#     mock_response = mock.Mock()
#     mock_response.status_code = 400
    
    
#     with pytest.raises(requests.HTTPError) :
#         service.get_users()