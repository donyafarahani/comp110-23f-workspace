"""defining a class"""

from __future__ import annotations

class Pizza:
    #attribute
    #think of these as varibales
    #
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, inp_size: str, inp_toppings: int, inp_gf:bool):
        #my constructor
        self.size = inp_size
        self.toppings = inp_toppings
        self.gluten_free = inp_gf

        #returns a Pizza object

    def price(self) -> float:
        """method to calculate price of pizza"""

        if self.size == 'large':
            price: float = 6.25
        else:
            price: float = 5.00
        price += .75 * self.toppings
        if self.gluten_free:
            price += 1.00
        return price
    
    def add_toppings(self, num_toppings: int) -> None:
        """Add toppings to existing pizza."""
        self.toppings += num_toppings

    
    def make_new_pizza_add_toppings(self, num_toppings: int) -> Pizza:
        """make new pizza with existing pizza's properties and add toppings."""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza