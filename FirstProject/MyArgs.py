def addition(*args):# Pass any number of arguments; args is a tuple
    return sum(args) * 0.05  # 5% of the sum of all arguments

print(addition(10, 20, 30, 40, 50))  # Example usage

print(addition(5, 15))  # Another example usage

print(addition())  # No arguments case          

print(addition(100, 200, 300))  # Another example usage with different numbers