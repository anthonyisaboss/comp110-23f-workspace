"""File to define River class."""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

__author__ = "730669473"


class River:
    """The hardest class ever."""
    day: int
    bears: list[Bear]
    fish: list[Fish]

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
        """Going too remove the fish And bears."""
        list1: list[Bear] = []
        list2: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                list2.append(fish)
        self.fish = list2
        for bear in self.bears:
            if bear.age <= 5:
                list1.append(bear)
        self.bears = list1
        return None
    
    def remove_fish(self, amount: int):
        """Going to remove the fish."""
        for fish in range(amount):
            if self.fish == self.fish:
                self.fish.pop(0)
        return None
    
    def bears_eating(self):
        """Having the bears eat fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Checking hunger of bears."""
        list1: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                list1.append(bear)
        self.bears = list1
        return None
        
    def repopulate_fish(self):
        """Going to repopulate the fish."""
        list2 = Fish()
        for _ in range(len(self.fish) // 2):
            for _ in range(4):
                self.fish.append(list2)
        return None
    
    def repopulate_bears(self):
        """Going to repopulate the bears."""
        list1 = Bear()
        for b in range(len(self.bears) // 2):
            self.bears.append(list1)
        return None
    
    def view_river(self):
        """Going to print out the view of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}") 
        print(f"Bear population: {len(self.bears)}")
        return None
    
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
        # RAHHH
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Noo docstring needed."""
        i: int = 0
        while i < 7:
            self.one_river_day()
            i += 1
        return None

            
