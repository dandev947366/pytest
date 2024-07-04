import math

def add(num_one, num_two):
    return num_one + num_two
    
def divide(num_one, num_two):
    if num_two == 0:
        raise ValueError("Division by zero is not allowed.")
    return num_one/num_two
    
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self): 
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
        
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
