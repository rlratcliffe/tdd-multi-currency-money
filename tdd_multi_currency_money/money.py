import logging
from tdd_multi_currency_money.expression import Expression
from tdd_multi_currency_money.bank import Bank

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tdd_multi_currency_money.sum import Sum

class Money(Expression):
    @property
    def amount(self) -> int:
        return self._amount

    @property
    def currency(self) -> str:
        return self._currency

    def __init__(self, amount: int, currency: str):
        self._amount: int = amount
        self._currency: str = currency

    def times(self, multiplier) -> Expression:
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: Expression) -> Expression:
        from tdd_multi_currency_money.sum import Sum
        return Sum(self, addend)

    @staticmethod
    def dollar(amount) -> 'Money':
        return Money(amount, "USD")

    @staticmethod
    def franc(amount) -> 'Money':
        return Money(amount, "CHF")

    def reduce(self, bank: Bank, to: str) -> 'Money':
        rate: int = bank.rate(self._currency, to)
        logging.debug("Rate is: " + str(rate))
        return Money(int(self._amount / rate), to)

    def __eq__(self, money: object):
        if not isinstance(money, Money):
            return NotImplemented

        logging.debug("Calculating: " + str(self._amount) + " == " + str(money.amount))
        return self._amount == money.amount and self._currency == money.currency