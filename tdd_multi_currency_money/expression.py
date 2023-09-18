from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tdd_multi_currency_money.bank import Bank

class Expression(ABC):
    
    def reduce(self, bank: 'Bank', to: str):
        pass