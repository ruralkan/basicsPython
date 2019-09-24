"""Model for aircraft flights"""
""" Validation and invariants"""

class Flight:
    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))
        
        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid rout '{}'".format(number))


        self._number = number
    
    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]


"""
In the REPL
from airtravel import Flight
g = Flight("SN060")
f = Flight("060")
f = Flight("sn060")
f = Flight("snabcd")
f = Flight("sn12345")

"""

