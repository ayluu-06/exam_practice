#!/usr/bin/python3


class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Pepe", 17) #instancia de la clase Person
person2 = Person("Brig", 14) # ''

print(person1.name) #acceder a los atr de instancia
print(person2.name) # ''

print(person1.age) #atr de inst x2
print(person2.age) # ''

print(person1.species) #acceder al atributo de clase
print(person2.species) # ''

person1.species = "Humanito normalito" #modificar el atributo a través de una instancia
print(person1.species) #acceder al atributo de clase
print(person2.species) # este se supone que no cambia

Person.species = "Gato"
print(person1.species) # este se queda normalito por estar sobreescito arriba
print(person2.species) # este si adquiere el valor nuevo desde la clase "base"