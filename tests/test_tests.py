import pytest
from tdd_multi_currency_money.money import Money
from tdd_multi_currency_money.franc import Franc

def test_dollar_multiplication():
    five = Money.dollar(5)
    assert Money.dollar(10) == five.times(2)
    assert Money.dollar(15) == five.times(3)

def test_franc_multiplication():
    five = Money.franc(5)
    assert Money.franc(10) == five.times(2)
    assert Money.franc(15) == five.times(3)

def test_equality():
    assert Money.dollar(5) == Money.dollar(5) 
    assert Money.dollar(5) != Money.dollar(6)
    assert Money.franc(5) == Money.franc(5) 
    assert Money.franc(5) != Money.franc(6)
    assert Money.franc(5) != Money.dollar(5)

def test_currency():
    assert "USD" == Money.dollar(1).currency
    assert "CHF" == Money.franc(1).currency

def test_different_class_equality():
    assert Money(10, "CHF") == Franc(10, "CHF")

def test_cannot_change_currency():
    with pytest.raises(AttributeError):
        five = Money.dollar(5)
        five.currency = "CHF"
        assert five.currency == "USD"

def test_cannot_change_amount():
    with pytest.raises(AttributeError):
        five = Money.dollar(5)
        five.amount = 6
        assert five.amount == 6