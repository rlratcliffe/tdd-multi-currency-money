from tdd_multi_currency_money.money import Money

class Dollar(Money):
    def __init__(self, amount):
        self._amount = amount
        self._currency = "USD"

    def times(self, multiplier):
        return Money.dollar(self._amount * multiplier)