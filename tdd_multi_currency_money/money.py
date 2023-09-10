import logging
from abc import ABC,abstractmethod

class Money(ABC):
    @property
    def amount(self):
        return self._amount

    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    @property
    def currency(self):
        return self._currency

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")

    def __eq__(self, money):
        # not sure how to cast here, money isn't type safe
        logging.debug("Calculating: " + str(self._amount) + " == " + str(money.amount))
        return self._amount == money.amount and self._currency == money.currency