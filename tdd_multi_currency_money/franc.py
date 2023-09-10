from tdd_multi_currency_money.money import Money

class Franc(Money):
    def __init__(self, amount):
        self._amount = amount

    def times(self, multiplier):
        return Franc(self._amount * multiplier)