myTuple = ("apple", "banana", "cherry")
print(myTuple[1])  # Output the second item in the tuple

#myTuple[1] = "orange"  # This will raise an error because ****tuples are immutable****
print(myTuple)

print(myTuple.count("banana"))  # Count occurrences of 'banana'
print(myTuple.index("cherry"))  # Find index of 'cherry'        
print(type(myTuple))


myTuple2 = ("Kiwi")
print(type(myTuple2))  # Output the type of myTuple2; it will be a string, not a tuple

myTuple3 = ("Kiwi",)  # Note the comma, this is a single-element tuple
print(type(myTuple3))  # Output the type of myTuple3; it will be a tuple