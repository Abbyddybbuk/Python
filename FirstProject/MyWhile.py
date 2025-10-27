x = 0

while x < 5:
    print(f"x is currently: {x}")
    x += 1
else:
    print("x is no longer less than 5")


y = [1, 2, 3] 

for item in y:
    # Do nothing
    pass # Using pass as a placeholder to indicate no operation and to avoid syntax error

print("Finished iterating through y")

myName = "Abhijeet Kulshreshtha"

for char in myName:
    if char == "K":
        continue  # Skip the rest of the loop when char is 'K'
    print(char)

myName = "Abhijeet Kulshreshtha"

for char in myName:
    if char == "K":
        break  # Exit the loop when char is 'K'
    print(char)    