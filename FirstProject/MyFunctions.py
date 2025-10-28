def print_msg(msg):
    print(f"Message: {msg}")

print_msg("Hello from MyFunctions.py")  

def add_numbers(a, b):
    return a + b    


result = add_numbers(5, 10)
print(f"The sum of 5 and 10 is: {result}")

def greet_user(name='Default User'):
    print(f"Hello, {name}!")
greet_user()

def sum_numbers(num1, num2):
    return num1 + num2  

print(f"Sum of 7 and 3 is: {sum_numbers('7', '3')}")#string concatenation due to string inputs


def is_even(num):
    return num % 2 == 0

print(f"Is 4 even? {is_even(4)}")
print(f"Is 7 even? {is_even(7)}")    