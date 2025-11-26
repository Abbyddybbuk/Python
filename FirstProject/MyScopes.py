#LEGB Rule: Local, Enclosing, Global, Built-in

name = "Global Name"

def greet():
    name = "Enclosing Name"
    
    def inner_greet():
        name = "Local Name"
        print("Hello,", name)  # Should print "Local Name"
    
    inner_greet()
    print("Hello again,", name)  # Should print "Enclosing Name"

greet()
print("Hello from the global scope,", name)  # Should print "Global Name"


# Demonstrating access to global variable
counter = 100

def increment_counter(counter):
    counter += 1  # This modifies the local copy of counter
    print("Inside function, counter:", counter)

    counter = 700  # This creates a new local variable named counter
    print("Inside function after reassignment, counter:", counter)

increment_counter(counter)
print("Outside function, counter:", counter)  # Should print 100, unchanged
