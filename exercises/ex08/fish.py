"""File to define Fish class."""


class Fish:
    """Class about fish."""
    
    age: int
    
    def __init__(self, f_age: int = 0):
        """The most painful thing ever."""
        self.age = f_age
        return None
    
    def one_day(self):
        """Worst thing ever."""
        self.age += 1
        return None