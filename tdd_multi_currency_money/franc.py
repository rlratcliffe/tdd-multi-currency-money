from tdd_multi_currency_money.money import Money

class Franc(Money):
    def __init__(self, amount):
        self._amount = amount
        self._currency = "CHF"

    def times(self, multiplier):
        return Money.franc(self._amount * multiplier)