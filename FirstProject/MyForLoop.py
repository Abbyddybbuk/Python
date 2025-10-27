myIterable = ["apple", "banana", "cherry"]

for item in myIterable:
    print(item)


myNumberIterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in myNumberIterable:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

sum=0        

for number in myNumberIterable:
    sum += number
print(f"The sum of numbers from 1 to 10 is {sum}")

myTestString = "Hello_World!"

for char in myTestString:
    print(char)


myTupleIterable = (10, 20, 30)

for item in myTupleIterable:
    print(item)

myTupList = [(1, 2), (3, 4), (5, 6), (7, 8)]    

for item in myTupList:
    print(item)

for (a, b) in myTupList:#tuple unpacking
    print(f"a: {a}, b: {b}")    

myDict = {"name": "Alice", "age": 30, "city": "New York"}

for key in myDict:
    print(f"Key: {key}, Value: {myDict[key]}")

for item in myDict.items():
    print(item)

for key,value in myDict.items():#tuple unpacking
    print(f"Key: {key}, Value: {value}")