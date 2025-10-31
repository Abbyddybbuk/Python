def myFunc(**kwargs):  # Accepts any number of keyword arguments; kwargs is a dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")


myFunc(name="Abhijeet", age=25, city="New York")  # Example usage


def myOtherFunc(*args, **kwargs):
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)
    print("I would like to order", args[0], "from", kwargs.get('restaurant', 'unknown restaurant'))

print(myOtherFunc(10, 20, restaurant="Pizzeria"))  # Example usage