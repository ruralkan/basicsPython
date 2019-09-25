class Aircraft:
    """
    The class is abstract in so far as it is never useful to instantiate it alone
    The class contains just the method we want to inherit into the derived classes.
    This class isn't usable on tis own because it depends on a method called seating_plan
    which isn't available at this level. Any attemp to use it standalone will fail
    """
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration
    
    def num_seat(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

class AirbusA319(Aircraft):
    
    def model(self):
        return "Airbus A319"
    
    def seating_plan(self):
        return range(1,23), "ABCDEF"

class Boeing77(Aircraft):

    def model(self):
        return "Boing 777"
    
    def seating_plan(self):
        # For simplicities sake, we ignore complex
        # seating arrangement for firs- class
        return range(1, 56), "ABCDEGHJK"