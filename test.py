import pytest
from main import add, divide, Circle, Rectangle
import math
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
        
def test_rec_area():
    rectangle = Rectangle(10, 20)
    assert rectangle.area() == 10 * 20

def test_rec_perimeter():
    rectangle = Rectangle(10, 20)
    assert rectangle.perimeter() == (10*2) + (20*2)
    
def test_circle_area():
    circle = Circle(10)
    assert circle.area() == math.pi * 10 ** 2
    
def test_circle_perimeter():
    circle = Circle(10)
    assert circle.perimeter() == 2 * math.pi * 10