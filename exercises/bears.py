"""River simulation."""

_author_ = "730464992"


class Bear:
    def __init__(self):
        self.age = 0
        self.hunger_score = 0


class Fish:
    def __init__(self):
        self.age = 0


class River:
    def __init__(self, num_fish, num_bears):
        self.day = 0
        self.bears = [Bear() for _ in range(num_bears)]
        self.fish = [Fish() for _ in range(num_fish)]


# river_simulation.py
from ex08.rivers import River

my_river = River(num_fish=10, num_bears=2)

class River:
    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")


