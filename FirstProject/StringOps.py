myString = "Hello, World!"

print(myString[-3])            # Output the string
print(myString[5])  

print(myString[:9]) #Output String upto index 9
print(myString[2:]) #Output String from index 2 to end

print(myString[::])# Output the whole string
print(myString[::2]) #Output every second character
print(myString[::-1]) #Output the string in reverse order


myString = "Hello World"
print(myString[-3])            # Output the string


myName = "Bbhijeet"
#myName[0] = "A"//It is not allowed as strings are immutable

my_Last_Letters = myName[1:]

print("A" + my_Last_Letters)

randomString = "Wow! This is really cool. Don't you think this is really awesome?"
randomString = "Hello!, " + randomString
print(randomString)# Output the string
print(randomString.upper()) #Output the string in uppercase

randomString = "Hi! This is a String Example."
print(randomString.split("i")) #Split the string from character 'i' and output as a list

