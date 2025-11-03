myNumList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def isEven(num):
    return num % 2 == 0

print(list(filter(isEven, myNumList)))

for item in filter(isEven, myNumList):
    print(item)


square=lambda num: num **2 #lambda function to calculate square of a number
print(square(4))

print(list(filter(lambda num: num % 2 == 0, myNumList)))#using lambda function with map to get squares of numbers in list

print(list(map(lambda num: num**2, myNumList)))#using lambda function with map to get squares of numbers in list