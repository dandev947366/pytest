import pytest
from main import add, divide

def test_add():
    result = add(1, 4)
    assert result == 5
    
def test_divide():
    result = divide(10, 5)
    assert result == 2
    
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)