print("This is a {} string".format("test"))
print("My {} is {} {}".format("SUV", "Blue", "Car"))
print("My {a} is a {b} {c}".format(c="SUV", b="Blue", a="Car"))

########################Formatting Numbers Using format() Method#########################################################
result = 100/666
print("The result is {}".format(result))
print("The result is {r:1.2f}".format(r=result))#formatted to show 2 decimal places with width of 1(spaces before number if needed)



########################Alternative Way to Format() Method(New in Python 3.6)#########################################################
name="Abhijeet"
print(f"His name is {name}")# Output the string and format using f-string method which helps in printing variables directly inside {}

#########################Formatting Numbers Using f-Strings#########################################################
name="John Doe"
age=25
print(f"{name} is {age} years old.");    