import logging

class Dollar:
    @property
    def amount(self):
        return self._amount

    def __init__(self, amount):
        self._amount = amount

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)

    def __eq__(self, dollar):
        # not sure how to cast here, dollar isn't type safe
        logging.debug("Calculating: " + str(self._amount) + " == " + str(dollar.amount))
        return self._amount == dollar.amount