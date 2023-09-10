import logging

class Money:
    @property
    def amount(self):
        return self._amount

    def __eq__(self, money):
        # not sure how to cast here, dollar isn't type safe
        logging.debug("Calculating: " + str(self._amount) + " == " + str(money.amount))
        return self._amount == money.amount and type(self) == type(money)