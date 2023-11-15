"""Defining a class."""
from __future__ import annotations

class Pizza:
    """Going to be a class to represent pizza."""

    #attributes
    #syntax <name> : <type>
    size: str
    toppings: int
    gluten_free: bool

    def __init__(self, size_input: str, toppings_input: int, gf_input, bool):
        """Constructor"""
        self.size = size_input
        self.toppings = toppings_input
        self.gluten_free = gf_input

    def price(self) -> float:
        """Method to compute price of pizza"""
        if self.size == "large":
            cost: float = 6.25
        else:
         cost: float = 5.00
        cost += .75 * self.toppings
        if self.gluten_free:
            cost += 1.00
        return cost
    
    def add_toppings(self, num_toppings: int):
        """Going to update existing order with num toppings."""
        self.toppings += num_toppings

    def add_toppings_new_order(self, num_toppings: int) -> Pizza:
        """Going to be adding toppings to a new order."""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza
