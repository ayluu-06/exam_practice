#!/usr/bin/python3

"""
class that defines an Animal with `name`, `species` attributes
"""


class Animal:


    def __init__(self, name, species): #constructor (no olvidar los dos puntos : )
        self.name = name
        self.species = species

    def make_sound(self):
        return f"Some generic sound"
    
class Dog(Animal):
    def make_sound(self):
        return "Woof!" #overriding Animal class

animal1 = Animal("animal name", "animal species")
dog1 = Dog("Poti", "Bichon Frisé")

print(animal1.make_sound())
print(dog1.make_sound())
