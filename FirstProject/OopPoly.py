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
    
    def blow_horn(self):
        raise NotImplementedError("This method should be overridden in subclasses")
    

myVehicle = Vehicle("Toyota", "Camry", 2021)


#print(myVehicle.blow_horn("Toyota", "Camry")) This will raise an error because blow_horn is not implemented

class Car(Vehicle):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    # Overriding the blow_horn method; implementing it for Car subclass 
    def blow_horn(self):
        return f"{self.make} {self.model} goes Beep Beep!"


myCar = Car("Honda", "Civic", 2020)
print(myCar.blow_horn())