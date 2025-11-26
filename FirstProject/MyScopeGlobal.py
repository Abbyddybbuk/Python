counter = 100

def increment_counter():
    global counter # Declare counter as global to modify the global variable
    counter += 1  # This modifies the global counter
    print("Inside function, counter:", counter)

    print("Modifying global counter to 700")
    counter = 700  # This modifies the global counter   
    print("Inside function after reassignment, Global counter is:", counter)

increment_counter()
print("Outside function, counter:", counter)  # Should print 700, modified