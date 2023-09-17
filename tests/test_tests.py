import pytest
import numpy as np
import logging
from tdd_multi_currency_money.money import Money
from tdd_multi_currency_money.bank import Bank
from tdd_multi_currency_money.sum import Sum
from tdd_multi_currency_money.pair import _Pair
from tdd_multi_currency_money.expression import Expression

def test_dollar_multiplication():
    five = Money.dollar(5)
    assert Money.dollar(10) == five.times(2)
    assert Money.dollar(15) == five.times(3)

def test_equality():
    assert Money.dollar(5) == Money.dollar(5) 
    assert Money.dollar(5) != Money.dollar(6)
    assert Money.franc(5) != Money.dollar(5)

def test_currency():
    assert "USD" == Money.dollar(1).currency
    assert "CHF" == Money.franc(1).currency

def test_reduce_money():
    bank = Bank()
    result = bank.reduce(Money.dollar(1), "USD")
    assert Money.dollar(1) == result

def test_plus_return_sum():
    five = Money.dollar(5)
    sum = five.plus(five)
    assert five == sum.augend
    assert five == sum.addend

def test_reduce_sum():
    sum = Sum(Money.dollar(3), Money.dollar(4))
    bank = Bank()
    result = bank.reduce(sum, "USD")
    assert Money.dollar(7) == result

def test_reduce_money_different_currency():
    bank = Bank()
    bank.addRate("CHF", "USD", 2)
    result = bank.reduce(Money.franc(2), "USD")
    assert Money.dollar(1) == result

def test_identity_rate():
    assert 1 == Bank().rate("USD", "USD")

def test_mixed_addition():
    fiveBucks: Expression = Money.dollar(5)
    tenFrancs: Expression = Money.franc(10)
    bank: Bank = Bank()
    bank.addRate("CHF", "USD", 2)
    result: Money = bank.reduce(fiveBucks.plus(tenFrancs), "USD")
    assert Money.dollar(10) == result

def test_simple_addition():
    five = Money.dollar(5)
    sum = five.plus(five)
    bank = Bank()
    reduced = bank.reduce(sum, "USD")
    assert Money.dollar(10) == reduced

# Helper/intermediary tests
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

def test_dict_with_key():
    newDict = dict()
    key = _Pair("CHF", "USD")
    newDict.update({key: int(2)})
    assert newDict.get(key) == 2
    assert newDict.get(_Pair("CHF", "USD")) == 2

def test_pairs_are_equal():
    assert _Pair("CHF", "USD") == _Pair("CHF", "USD")

def test_array_equals():
    array = []
    array.append({"abc"})
    arrayTwo = []
    arrayTwo.append({"abc"})
    assert array == arrayTwo
    assert np.array({"abc"}) == np.array({"abc"})

def test_dict_with_key_as_str():
    newDict = dict()
    newDict.update({"TestKey": int(2)})
    assert newDict.get("TestKey") == 2