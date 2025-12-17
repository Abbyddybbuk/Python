class Vehicle():
    
    ## Class/Static Attribute
    vehicleType = "Car" 
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    #Passing self as parameter means that this is an instance method
    def start_engine(self):
        return f"The engine of the {self.year} {self.make} {self.model} is starting."
    
    #Passing self as parameter means that this is an instance method
    def stop_engine(self):
        return f"The engine of the {self.year} {self.make} {self.model} is stopping."
    
    #Static Method
    def blow_horn(make, model):
        return f"{make} {model} goes Beep Beep!"
    
myCar1= Vehicle("Seat", "Taracco", 2020)
print(myCar1.start_engine(), f"Type: {myCar1.vehicleType}")    

myCar2= Vehicle(make="BMW", model="X5", year=2022)
print(myCar2.start_engine(), f"Type: {myCar2.vehicleType}") 
print(myCar1.stop_engine())
#print(myCar2.blow_horn("Audi", "Q7"))// This will raise an error because blow_horn is not an instance method
print(Vehicle.blow_horn("Audi", "Q7"))  # Correct way to call the static method