#!/usr/bin/python3

"""
class that defines a car with `brand`, `model`, `year` attributes
"""


class Car:


    def __init__(self, brand, model, year): #constructor (no olvidar los dos puntos : )
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self): #method
        return f"{self.brand}, {self.model}, {self.year}"

car1 = Car("audi", "a6", 2013) #objeto (no olvidar comas entre objetos)
print(car1.display_info()) #llamar objeto