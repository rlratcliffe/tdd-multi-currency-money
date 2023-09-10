from tdd_multi_currency_money.dollar import Dollar

def test_multiplication():
    five = Dollar(5)
    product = five.times(2)
    assert 10 == product.amount
    product = five.times(3)
    assert 15 == product.amount
