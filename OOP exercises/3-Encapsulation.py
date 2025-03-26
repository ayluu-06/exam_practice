#!/usr/bin/python3

"""
class that defines BankAccount with __balance private attribute
"""


class BankAccount:


    def __init__(self, balance):
        self.__balance = balance #private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
account1 = BankAccount(300)
account1.deposit(200)
account1.withdraw(100)

print(account1.get_balance())
print(account1.__balance()) #atributo privado, no va a dejar acceder(error)
