import pytest
from main import add, divide, Circle, Rectangle
import math
import time
def test_add():
    result = add(1, 4)
    assert result == 5
    
def test_add_string():
    result = add('i like ', 'burgers')
    assert result == 'i like burgers'
    
def test_divide():
    result = divide(10, 5)
    assert result == 2
    
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
             
class TestCircle:
    def setup_method(self, method):
        self.circle = Circle(10)
        
    def test_area(self):
        result = math.pi * self.circle.radius ** 2
        assert self.circle.area() == result
        
    def test_perimeter(self):
        result = 2 * math.pi * self.circle.radius
        assert self.circle.perimeter() == result
        
@pytest.fixture
def my_rectangle():
    return Rectangle(10, 20)
    
@pytest.fixture
def my_weird_rectangle():
    return Rectangle(5, 6)
    
def test_rec_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20

def test_rec_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == (10*2) + (20*2)
    
def test_not_equal(my_rectangle, my_weird_rectangle):
    assert my_rectangle != my_weird_rectangle
    
@pytest.fixture
def my_circle():
    return Circle(10)
    
def test_circle_area(my_circle):
    assert my_circle.area() == math.pi * 10 ** 2

def test_circle_perimeter(my_circle):
    assert my_circle.perimeter() == 2 * math.pi * 10
    
def test_not_same_area_rec(my_circle, my_rectangle):
    assert my_circle.area() != my_rectangle.area()
    
@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = divide(10, 5)
    assert result == 2
    
@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert add(1, 2) == 3
    
@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_by_zero():
    divide(10,0)