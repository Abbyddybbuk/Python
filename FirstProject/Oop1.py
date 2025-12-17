class Sample():
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")

myObject = Sample(10)
myObject.display()

print(type(myObject))