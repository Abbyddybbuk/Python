class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        if self.species == "Dog":
            return "Woof!"
        elif self.species == "Cat":
            return "Meow!"
        else:
            return "Unknown sound"
        
myDog = Animal("Buddy", "Dog")
print(f"{myDog.name} is a {myDog.species} and says: {myDog.make_sound()}")        