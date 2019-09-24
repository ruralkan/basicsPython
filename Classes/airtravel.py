"""Model for aircraft flights"""
""" Collaborating classes"""
"""
The law of Demeter is an object- oriented design principle that says you should never
call methods on objcts you receive from other calls. O, put another way: Only talk to
your immediate friend

We'll now modify our Flight class to accept an aircraft object when it is constructed,
and we'll follow the Law of Demeter by adding a method to report the aircraft model.
This method delegate to Aircraft on bhelaf of the client rater than allowing the client 
to "reach through" the Fligth and interrogate the Aircraft object directly.
"""

class Flight:
    """A flight with a particular passenger aircraft"""

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))
        
        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid rout '{}'".format(number))

        self._number = number
        self._aircraft = aircraft
    
    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]
    
    def aircraft_model(self):
        return self._aircraft.model()



class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration
        
    def model(self):
        return self._model
        
    def seating_plan(self):
        return (range(1, self._num_rows + 1), 
                "ABCDEFGHJK"[:self._num_seat_per_row])


"""
In the REPL
from airtravel import *
f = Flight("BA758",Aircraft("G-EUPT", "Airbus A319", num_rows=22,
            num_seats_per_row=6))
f.aircraft()
"""

