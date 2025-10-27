for num in range(1, 11):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


for num in range(1, 101, 2):#step of 2(skipping even numbers)
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")        


print(list(range(1, 11, 2)))        


myName = "Abhijeet Kulshreshtha"

for item in enumerate(myName):
    print(item) #prints tuple of (index, character)


for index, char in enumerate(myName):#tuple unpacking
    print(f"Index: {index}, Character: {char}") 

myList1 = ["a", "b", "c"]
myList2 = [1, 2, 3, 4]     

for item in zip(myList1, myList2):
    print(item) #prints tuple of (item from list1, item from list2); stops at the shortest list which means 4 will be ignored

print(list(zip(myList1, myList2))) 


myCharList = ['a', 'b', 'c', 'd', 'e', 'x']

if ('x' in myCharList):
    print("x is present in the list")
else:
    print("x is not present in the list")

myMsg = "Hello, welcome to the world of Python programming."

if ('H' in myMsg):
    print("H is present in the message")
else:
    print("H is not present in the message")    


myDict = {"name": "Alice", "age": 30, "city": "New York"}

if ("Sex" in myDict):
    print("Sex key is present in the dictionary")   
else:
    print("Sex key is not present in the dictionary")    