"""Model for aircraft flights"""
"""Counting available seats"""

class Flight:
    """We'll perform a small refactoring and extract the seat designator parsing 
    validaton logic into ait's own method parse_seat()"""

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))
        
        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid rout '{}'".format(number))

        self._number = number
        self._aircraft = aircraft
        # we retrieve the seating plan for the aricraft and use tuple unpacking to put
        # the row and seat identiiers into local variables rows and seats
        # In the second line we create a list for the seat allocation
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]
    
    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]
    
    def aircraft_model(self):
        return self._aircraft.model()
    
    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger
        
        Args:
            seat: A seat designator such as '12C' or '21F'
            passenger: The passenger name
        
        Raises:
            ValueError: If the seat is unavailable
        """
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger
    

    def _parse_seat(self, seat):
        """Parse a seat designator into a valid row and letter
        
        Args:
            seat: A seat designator such as 12F

        Returns:
            A tuple containing an integer, string for row and seat
        """
        rows, seat_letters  = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))
        
        return row, letter
    
    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passenger to a different seat
        Args:
            from_seat: The existing seat designator for 
                       the passenger to be moved
            
            to_seat: The new seat designator.
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate in seat {}".format(from_seat))
        
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("already occupied {}".format(to_seat))
        
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None) for row in self._seating if row is not None)



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
                "ABCDEFGHJK"[:self._num_seats_per_row])



def make_flight():
    f = Flight("BA758",Aircraft("G-EUPT", "Airbus A319", num_rows=22,
            num_seats_per_row=6))
    f.allocate_seat('12A', 'Guido Van Rossum')
    f.allocate_seat('15F', 'Bjarne Stroustrup')
    f.allocate_seat('15E', 'Anders Hejsberg')
    f.allocate_seat('1C', 'Jhon McCarthy')
    f.allocate_seat('1D', 'Richard Hickey')
    return f

"""
In the REPL
from airtravel import make_flight
f = make_flight()
f.relocate_passenger('12A', '15D')
from pprint import pprint as pp
pp(f._seating)
f.num_available_seats()
"""

