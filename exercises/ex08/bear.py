"""File to define Bear class."""

_author_ = "730464992"


class Bear:
    """Define Bears."""
    
    def __init__(self):
        """Set bear age and hunger score."""
        self.age = 0
        self.hunger_score = 0
    
    def one_day(self):
        """Increase bear age by 1."""
        self.age += 1

    def eat(self, num_fish: int):
        """Hunger score defined by number of fish present."""
        self.hunger_score += num_fish