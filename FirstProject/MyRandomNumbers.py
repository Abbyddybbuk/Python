from random import shuffle

myNumlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

shuffle(myNumlist) # does not return a new list; it shuffles the existing list in place
print("Original list:", myNumlist)


from random import randint

print(randint(1, 100))  # prints a random integer between 1 and 100 (both inclusive)

input("Press Enter to exit...")

myMsg = input("Type a message for me......")
print("You typed:", myMsg)