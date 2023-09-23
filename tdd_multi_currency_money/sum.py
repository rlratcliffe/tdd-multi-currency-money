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

    # mypy failing since this is returning nothing for now
    # add '-> Expression' return type back later
    def plus(self, addend: Expression):
        pass