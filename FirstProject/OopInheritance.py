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
    
class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)  # Call the constructor of the parent class
        self.battery_capacity = battery_capacity  # New attribute for ElectricVehicle
    
    # Overriding the start_engine method
    def start_engine(self):
        return f"The electric engine of the {self.year} {self.make} {self.model} is starting silently."
    
    # New method specific to ElectricVehicle
    def charge_battery(self):
        return f"The battery of the {self.year} {self.make} {self.model} is charging."
    
    # Overriding the stop_engine method
    def stop_engine(self):
        return f"The engine of the {self.year} {self.make} {self.model} is switching off silently."    
    
myVehicle = Vehicle("Toyota", "Camry", 2021)
print(myVehicle.start_engine(), f"Type: {myVehicle.vehicleType}")

myElectricVehicle = ElectricVehicle("Tesla", "Model S", 2022, "100 kWh")
print(myElectricVehicle.start_engine(), f"Type: {myElectricVehicle.vehicleType}")
print(myElectricVehicle.charge_battery())
print(myElectricVehicle.stop_engine())  

print(myVehicle.stop_engine())


for instance in (myVehicle, myElectricVehicle):
    print(f"{instance.make} is instance of Vehicle: {isinstance(instance, Vehicle)}")
    print(f"{instance.make} is instance of ElectricVehicle: {isinstance(instance, ElectricVehicle)}")