def calcSqaure(num):
    return num * num    

myNumList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in map(calcSqaure, myNumList):# Here calcSqaure is not called like calcSqaure(); instead the function itself is passed as an argument to map()
    print(item)

print(list(map(calcSqaure, myNumList)))    

print(map)

def checkStringLength(myString):
    if len(myString)%2 == 0:
        return "Even String"
    else:
        return 0
    
myStringList = ["Abhijeet", "Kulshreshtha", "Joe", "Rio", "Python"]

print(list(map(checkStringLength, myStringList)))# can return mixed types in list

