from tdd_multi_currency_money.money import Money

class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)