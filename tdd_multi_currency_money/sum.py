from tdd_multi_currency_money.money import Money
from tdd_multi_currency_money.expression import Expression
from tdd_multi_currency_money.bank import Bank

class Sum(Expression):
    @property
    def augend(self):
        return self._augend

    @property
    def addend(self):
        return self._addend

    def __init__(self, augend: Money, addend: Money):
        self._augend = augend
        self._addend = addend

    def reduce(self, bank: Bank, to):
        amount = self._augend.amount + self._addend.amount
        return Money(amount, to)