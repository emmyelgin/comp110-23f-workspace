"""File to define River class."""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


_author_ = "730464992"


class River:  
    """Defining River."""

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Update self.fish and self.bears with new lists."""
        # Assuming this is within the River class in river.py
        new_fish_list = [fish for fish in self.fish if fish.age <= 3]
        new_bear_list = [bear for bear in self.bears if bear.age <= 5]
        self.fish = new_fish_list
        self.bears = new_bear_list
    
    def bears_eating(self):
        """Keep track of how many fish bears eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3) 
        return None
    
    def check_hunger(self):
        """Check bears hunger level."""
        new_bear_list = []
        for bears in self.bear:
            if Bear.hunger_score >= 0:
                new_bear_list.append(Bear)
        self.bears = new_bear_list
        return None
        
    def repopulate_fish(self):
        """Count fish offspring."""
        num_fish = len(self.fish)
        new_num_fish = (num_fish // 2) * 4
        for i in range(new_num_fish):
            new_fish = Fish()
            self.fish.append(new_fish)
        return None
    
    def repopulate_bears(self):
        """Count bear offspring."""
        num_bears = len(self.Bears)
        new_num_bears = (num_bears // 2)
        for i in range(new_num_bears):
            new_bears = Bear()
            self.bears.append(new_bears)
        return None
    
    def view_river(self):
        """Print river status."""
        print(f"~~~ Day {self.day}: ~~~~.")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate a week in the river."""
        for _ in range(7):
            self.one_river_day()
        self.day = 7
            
    def remove_fish(self, amount: int):
        """Remove appropraite amount of fish."""
        self.fish = self.fish[amount]
