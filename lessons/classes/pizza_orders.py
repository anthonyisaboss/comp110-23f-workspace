"""Instating a class."""

from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 10, True) #constructor

#access/set/update attribute values

print(Pizza.size)


sals_pizza: Pizza = Pizza("medium", 5, False)


def price(input_pizza: Pizza) -> float:
    """Compute the price of the pizza"""
    if input_pizza.size == "large":
        cost: float = 6.25
    else:
        cost: float = 5.00
    cost += .75 * input_pizza.toppings
    if input_pizza.gluten_free:
        cost += 1.00
    return cost

print(my_pizza.price())
print(sals_pizza.price())

print(my_pizza.add_toppings(3))
print(my_pizza.price())

my_second_pizza: Pizza = my_pizza.add_toppings_new_order(2)
print(my_second_pizza.toppings)

