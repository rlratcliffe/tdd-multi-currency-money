import logging
from abc import ABC,abstractmethod

class Money(ABC):
    @property
    def amount(self):
        return self._amount

    @abstractmethod
    def times(muliplier):
        pass

    @property
    def currency(self):
        return self._currency

    @staticmethod
    def dollar(amount):
        from tdd_multi_currency_money.dollar import Dollar
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        from tdd_multi_currency_money.franc import Franc
        return Franc(amount)

    def __eq__(self, money):
        # not sure how to cast here, dollar isn't type safe
        logging.debug("Calculating: " + str(self._amount) + " == " + str(money.amount))
        return self._amount == money.amount and type(self) == type(money)