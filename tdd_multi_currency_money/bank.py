from tdd_multi_currency_money.expression import Expression
from tdd_multi_currency_money.pair import _Pair

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tdd_multi_currency_money.money import Money

class Bank:
    @property
    def rates(self) -> dict:
        return self._rates

    def __init__(self):
        self._rates = dict()

    def reduce(self, source: Expression, to: str) -> 'Money':
        return source.reduce(self, to)

    def addRate(self, strFrom: str, strTo: str, rate: int) -> None:
        newInputToDict= {_Pair(strFrom, strTo): int(rate)}
        self._rates.update(newInputToDict)

    def rate(self, strFrom: str, strTo: str) -> int:
        return 1 if strFrom == strTo else self._rates.get(_Pair(strFrom, strTo))