#!/usr/bin/python3


class Calculator:

    @staticmethod
    def add(a, b):
        return a + b #se define el comportamiento(?
    
    @classmethod
    def create_default(cls):
        return cls() #crea un default instance(?

result = Calculator.add(5, 3)
print(f"The sum of 5 and 3 is: {result}") #imprime el resultado de la suma

default_calculator = Calculator.create_default() #llama a la funcion para que cree el default ese
print(f"Default calculator instance created: {default_calculator}") #lo imprime :)