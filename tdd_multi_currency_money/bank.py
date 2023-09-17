from tdd_multi_currency_money.expression import Expression
from tdd_multi_currency_money.pair import _Pair

class Bank:
    @property
    def rates(self):
        return self._rates

    def __init__(self):
        self._rates = dict()

    def reduce(self, source: Expression, to: str):
        return source.reduce(self, to)

    def addRate(self, strFrom, strTo, rate):
        newInputToDict= {_Pair(strFrom, strTo): int(rate)}
        self._rates.update(newInputToDict)

    def rate(self, strFrom, strTo) -> int:
        return self._rates.get(_Pair(strFrom, strTo))