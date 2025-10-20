myTuple = ("apple", "banana", "cherry")
print(myTuple[1])  # Output the second item in the tuple

#myTuple[1] = "orange"  # This will raise an error because tuples are immutable
print(myTuple)

print(myTuple.count("banana"))  # Count occurrences of 'banana'
print(myTuple.index("cherry"))  # Find index of 'cherry'        
print(type(myTuple))
