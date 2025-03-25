#!/usr/bin/pytrhon3

"""
class that defines a car with `brand`, `model`, `year` attributes
"""

class Car:
    def __init__(self, brand, model, year): #constructor
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self): #method
        print({self.brand}, {self.model}, {self.year})
