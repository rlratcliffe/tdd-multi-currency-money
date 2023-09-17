import logging
from tdd_multi_currency_money.money import Money
from tdd_multi_currency_money.expression import Expression

class Sum(Expression):
    @property
    def augend(self: Expression):
        return self._augend

    @property
    def addend(self: Expression):
        return self._addend

    def __init__(self, augend: Expression, addend: Expression):
        self._augend = augend
        self._addend = addend

    def reduce(self, bank: 'Bank', to):
        amount = self._augend.reduce(bank, to).amount \
        + self._addend.reduce(bank, to).amount
        return Money(amount, to)