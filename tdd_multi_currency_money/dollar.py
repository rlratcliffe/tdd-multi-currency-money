from tdd_multi_currency_money.money import Money

class Dollar(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def times(self, multiplier):
        return Money.dollar(self._amount * multiplier)