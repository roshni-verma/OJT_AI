import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Example usage:
rectangle = Rectangle(5, 3)
print(f"Area of Rectangle: {rectangle.area()}")

circle = Circle(4)
print(f"Area of Circle: {circle.area()}")
