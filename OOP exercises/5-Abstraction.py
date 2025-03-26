#!/usr/bin/python3

from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"credit card payment of ${amount}")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"PayPal payment of ${amount}")

payment1 = CreditCardPayment()
payment1.process_payment(100)

payment2 = PayPalPayment()
payment2.process_payment(50)