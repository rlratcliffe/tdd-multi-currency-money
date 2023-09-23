from tdd_multi_currency_money.money import Money
from tdd_multi_currency_money.expression import Expression
from tdd_multi_currency_money.bank import Bank

class Sum(Expression):
    @property
    def augend(self) -> Money:
        return self._augend

    @property
    def addend(self) -> Money:
        return self._addend

    def __init__(self, augend: Money, addend: Money):
        self._augend: Money = augend
        self._addend: Money = addend

    def reduce(self, bank: Bank, to):
        amount = self._augend.amount + self._addend.amount
        return Money(amount, to)