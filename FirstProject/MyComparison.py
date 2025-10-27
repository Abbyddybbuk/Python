num1 = 3
num2 = 5

if num1 > num2:
    print(f"{num1} is greater than {num2}") 
else:
    print(f"{num2} is greater than {num1}")


if not(num1 > num2):
    print(f"{num2} is greater than {num1}") 
else:   
    print(f"{num1} is greater than {num2}")

num1 = 7
num2 = 7

if num1 < num2:
    print(f"{num1} is less than {num2}")    
elif num1 == num2:
    print(f"{num1} is equal to {num2}") 
else:
    print(f"{num1} is greater than {num2}")