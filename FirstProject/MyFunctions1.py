numList = list(range(1,101))

def is_any_number_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return True
        else:
            pass
    return False

print(f"Is any number even in {numList}? {is_any_number_even(numList)}")        

def return_number_even(numbers):
    resultList = []
    for num in numbers:
        if num % 2 == 0:
          resultList.append(num)
    return resultList      

print(f"Even numbers from 1 to 100 are: {return_number_even(numList)}")      
        