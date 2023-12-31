from abc import ABC,abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tdd_multi_currency_money.bank import Bank
    from tdd_multi_currency_money.money import Money

class Expression(ABC):
    @abstractmethod
    def plus(self, addend: 'Expression') -> 'Expression':
        pass

    @abstractmethod
    def reduce(self, bank: 'Bank', to: str) -> 'Money':
        pass

    @abstractmethod
    def times(self, multiplier: int) -> 'Expression':
        pass