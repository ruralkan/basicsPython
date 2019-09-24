"""Model for aircraft flights"""

class Flight:
    def __init__(self, number):
        """" we use leading underscore by convention the implementation details of
        objects which are not intended for consumtion or manipulation by clients
        of the objects should be prefixed with underscore
        """
        self._number = number
    
    def number(self):
        return self._number


"""
In the REPL
from airtravel import Flight
g = Flight("SN060")
g.number()
"""

