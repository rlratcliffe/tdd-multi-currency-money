import logging

class Dollar:
    amount = None

    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def equals(self, dollar):
        # not sure how to cast here, dollar isn't type safe
        logging.debug("Calculating: " + str(self.amount) + " == " + str(dollar.amount))
        return self.amount == dollar.amount