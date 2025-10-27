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


if ("Alice" in myDict.values()):
    print("Alice value is present in the dictionary")   
else:
    print("Alice value is not present in the dictionary")

myNumList = [10, 20, 30, 40, 50]
print(min(myNumList))  # Output: 10
print(max(myNumList))  # Output: 50