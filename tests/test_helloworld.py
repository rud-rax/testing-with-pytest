import pytest

import src.helloworld.helloworld as helloworld


def test_add():
    
    s = helloworld.add(1,4)
    assert s == 5
    
def test_add_strings():
    s = helloworld.add('i like' , ' burgers')
    assert s == 'i like burgers'
    
def test_divide():
    s = helloworld.divide(10 , 5)
    assert s == 2
    
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) : 
        helloworld.divide(1 , 0)