myList = ["Abhi", 100, 200.5, True]

print(myList[-1])  # Output the last element
print(myList[1:3])  # Output elements from index 1 to 2

myList_temp = ["Kuls", 300, 400.5, False]


myList_temp[0] = myList_temp[0].upper()  # Change first element to uppercase
myListResult = myList + myList_temp  # Concatenate two lists
print(myListResult)  # Output the concatenated list

myListResult.append("New Element")  # Add a new element to the end of the list
print(myListResult)  # Output the updated list

popped_item=myListResult.pop()  # Remove the last element
print(myListResult)  # Output the list after removing the last element
print(popped_item)  # Removed last element


myListResult.pop(2)  # Remove element at index 2
print(myListResult)  # Output the list after removing the element at index 2

char_list = ['a', 'x', 'm', 'd', 'e']
num_list = [5, 3, 8, 1, 4]
char_list.sort() # Sort the character list but return None Object
num_list.sort()  # Sort the character list but return None Object
print(char_list)  # Output sorted character list
print(num_list)  # Output sorted number list

tempList=char_list.sort()
print(type(tempList))

num_list.reverse()  # Reverse the number list
print(num_list)  # Output reversed number list  