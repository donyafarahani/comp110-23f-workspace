"""File to define Bear class."""


class Bear:
    """Class for creating bears."""
    def __init__(self, age: int = 0, hunger_score: int = 0):
        """Constructor."""
        self.age = age
        self.hunger_score = hunger_score
        return None
    
    def one_day(self):
        """Adds 1 to age and subtracts 1 from hunger_score daily."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """When bear eats num_fish, hunger_score increases by num_fish."""
        self.hunger_score += num_fish
        return None