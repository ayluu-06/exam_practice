#!/usr/bin/python3

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Función que usa polimorfismo
def print_area(shape):
    print(f"Area: {shape.area()}")


# Crear objetos
rectangle = Rectangle(5, 10)
circle = Circle(3)

# Probar polimorfismo
print_area(rectangle)
print_area(circle)

# Imprimir más información
print("Perimeter:", rectangle.perimeter())
print("Diagonal:", rectangle.calculate_diagonal())
print("Perimeter:", circle.perimeter())



import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Testing with instances
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Circle area: {circle.area()}")
print(f"Rectangle area: {rectangle.area()}")