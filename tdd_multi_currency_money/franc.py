import logging

class Franc:
    @property
    def amount(self):
        return self._amount

    def __init__(self, amount):
        self._amount = amount

    def times(self, multiplier):
        return Franc(self._amount * multiplier)

    def __eq__(self, franc):
        # not sure how to cast here, franc isn't type safe
        logging.debug("Calculating: " + str(self._amount) + " == " + str(franc.amount))
        return self._amount == franc.amount