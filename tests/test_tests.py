from tdd_multi_currency_money.dollar import Dollar

def test_multiplication():
    five = Dollar(5)
    five.times(2)
    assert 10 == five.amount
