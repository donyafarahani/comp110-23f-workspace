"""File to define Fish class."""


class Fish:
    """Creates fish and ages fish daily."""
    def __init__(self, age: int = 0):
        """Constructor."""
        self.age = age
        return None
    
    def one_day(self):
        """Adds 1 to age each day."""
        self.age += 1
        return None