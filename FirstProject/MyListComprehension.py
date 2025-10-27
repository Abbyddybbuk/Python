myMsg = "My favorite numbers are 3, 7, and 21.";

myList = []

for char in myMsg:
    myList.append(char.upper())

print(myList)    

myListComp = [char.upper() for char in myMsg]#list comprehension version of above code
print(myListComp)   


myNameList = [char for char in "Abhijeet Kulshreshtha"]#list comprehension
print(myNameList)

myNumList = [num **2 for num in range(1, 11)]#squares of numbers from 1 to 10
print(myNumList)    

myNumList = [num **2 for num in range(1, 11) if num % 2 == 0]#squares of even numbers from 1 to 10
print(myNumList)   

celsiusList = [0, 10, 20, 30, 40, 50]
fahrenheitList = [ ( (9/5) * temp + 32 ) for temp in celsiusList ]#convert celsius to fahrenheit
print(fahrenheitList)


myNumList = [num **2 if num % 2 == 0 else 'ODD'for num in range(1, 11) ]#squares of even numbers and 'ODD' for odd numbers from 1 to 10
print(myNumList)   

myTestList = []

for x in [2,3,4]:
    for y in [100, 200, 300]:
        myTestList.append(x * y)
print(myTestList)   


myTestListComp = [x * y for x in [2,3,4] for y in [100, 200, 300]]#list comprehension version of above code
print(myTestListComp)