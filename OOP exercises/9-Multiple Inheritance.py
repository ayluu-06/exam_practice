#!/usr/bin/python3


class Flyable:
    def fly(self):
        print("fly?")

class Swimmable:
    def swim(self):
        print("swim?")

class Duck(Flyable, Swimmable):
    pass

duck = Duck()

duck.fly()
duck.swim()

