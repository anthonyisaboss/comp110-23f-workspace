"""File to define Bear class."""


class Bear:
    """Class about bears."""

    age: int
    hunger_score: int
    
    def __init__(self, b_age: int = 0, points: int = 0):
        """A painful func."""
        self.age = b_age
        self.hunger_score = points
        
        return None
    
    def one_day(self):
        """Even more painful func."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Going to show that the bears eat."""
        self.hunger_score += num_fish
