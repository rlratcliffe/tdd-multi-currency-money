from tdd_multi_currency_money.expression import Expression
from tdd_multi_currency_money.money import Money

class Bank:
    
    def reduce(self, source: Expression, to: str):
        return source.reduce(to)