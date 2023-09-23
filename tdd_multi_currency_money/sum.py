from tdd_multi_currency_money.money import Money
from tdd_multi_currency_money.expression import Expression
from tdd_multi_currency_money.bank import Bank

class Sum(Expression):
    @property
    def augend(self) -> Expression:
        return self._augend

    @property
    def addend(self) -> Expression:
        return self._addend

    def __init__(self, augend: Expression, addend: Expression):
        self._augend: Expression = augend
        self._addend: Expression = addend

    def reduce(self, bank: Bank, to):
        amount = self._augend.reduce(bank, to).amount \
        + self._addend.reduce(bank, to).amount
        return Money(amount, to)

    def plus(self, addend: Expression) -> Expression:
       return Sum(self, addend)

    def times(self, multiplier: int) -> Expression:
        return Sum(self._augend.times(multiplier), self._addend.times(multiplier))