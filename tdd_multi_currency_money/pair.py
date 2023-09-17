class _Pair:
    @property
    def strFrom(self):
        return self._strFrom

    @property
    def strTo(self):
        return self._strTo

    def __init__(self, strFrom, strTo):
        self._strFrom = strFrom
        self._strTo = strTo

    def __eq__(self, __o: object) -> bool:
        return self._strFrom == __o.strFrom and self._strTo == __o.strTo
    
    def __hash__(self) -> int:
        return 0