mySet = set(["apple", "banana", "cherry"])
print(mySet)  # Output the set

mySet.add("orange")  # Add an item to the set
print(mySet)  # Output the updated set

mySet.add("banana")  # Try to add a duplicate item
print(mySet)  # Output the set to show no duplicates    

myList = ["kiwi", "mango", "grape", "apple", "kiwi"]
mySetFromList = set(myList)  # Create a set from a list

print(mySetFromList)  # Output the set created from the list
print(myList)  # Output the original list to show it still has duplicates

