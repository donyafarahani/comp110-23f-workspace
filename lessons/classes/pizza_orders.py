"""used to create instances of a class: instantiating a class."""

from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 10, True) # constructor 
#type is pizza because the class is like a new type

#accessing/setting attributes
#my_pizza.size = "large"
#my_pizza.toppings = 10
#y_pizza.gluten_free = True

#printing out some values
print("my pizza: ")
print(my_pizza)

print("Pizza:")
print(Pizza)

print("size attribute:")
print(my_pizza.size)

print(my_pizza.toppings)

sals_pizza: Pizza = Pizza('medium', 5, False)
print(sals_pizza.size)

def price(input_pizza: Pizza) -> float:
    """function to calculate price of pizza"""
    if input_pizza.size == 'large':
        price: float = 6.25
    else:
        price: float = 5.00
    price += .75 * input_pizza.toppings
    if input_pizza.gluten_free:
        price += 1.00

    return price

#calling price function
print(price(sals_pizza))

#calling price method
print(sals_pizza.price())

my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())

my_other_pizza: Pizza = my_pizza.make_new_pizza_add_toppings(2)
print(my_other_pizza.toppings)
print(my_pizza.toppings)


