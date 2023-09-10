from tdd_multi_currency_money.money import Money

class Dollar(Money):
    def __init__(self, amount):
        self._amount = amount

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)