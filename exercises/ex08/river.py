"""File to define River class."""

__author__ = "730661618"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Building of river simulation."""
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
        """Checks age of each Fish and Bear."""
        fish_copy: list[Fish] = []
        for f in self.fish:
            if f.age <= 3: 
                fish_copy.append(f)
        self.fish = fish_copy
        
        bears_copy: list[Bear] = []
        for b in self.bears:
            if b.age <= 5: 
                bears_copy.append(b)
        self.bears = bears_copy
        return None
    
    def remove_fish(self, amount: int):
        """Removes amount many Fish from the River, starting from index 0."""
        for f in range(amount):
            self.fish.pop(0)
        return None

    def bears_eating(self):
        """Simulates a bear eating if theres at least 5 fish in river."""
        for b in self.bears:
            if len(self.fish) >= 5:
                b.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Checks hunger of each bear and removes them if hunger is less than 0."""
        bears_copy: list[Bear] = []
        for b in self.bears:
            if b.hunger_score >= 0:
                bears_copy.append(b)
        self.bears = bears_copy
        return None
    
    def repopulate_fish(self):
        """Reproduction of fish."""
        offspring_num: int = (len(self.fish) // 2) * 4
        for num in range(offspring_num):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Reproduction of bears."""
        offspring_num: int = (len(self.bears)) // 2
        for num in range(offspring_num):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Output of day, fish population, and bear population."""
        print(f"~~~ Day {self.day}: ~~~\nFish population: {len(self.fish)}\nBear population: {len(self.bears)}")

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
        """Simulates one week in the river."""
        for x in range(0, 7):
            self.one_river_day()
        return None