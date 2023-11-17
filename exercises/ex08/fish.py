"""File to define Fish class."""

_author_ = "730464992"


class Fish:
    """Define Fish."""
    
    def __init__(self):
        """Set fish age to 0."""
        self.age = 0
        return None

    def one_day(self):
        """Increase age by 1 with each day."""
        self.age += 1
        return None