# creating a Zoo Management System using Python classes

class Animal:

    def __init__(self,name,species,age):
        self.name = name
        self.species =species
        self.age = age

    def Print(self):
        print(f"Parent Animal Name: {self.name} Specie :{self.species} and Age :{self.age}!")
        
class Mammal(Animal):

    def __init__(self,name,species,age,sound):

        self.sound = sound
        super().__init__(name,species,age)

    def make_sound(self):

        print(f"Sound of the {self.name} is {self.sound}.")

    def Print(self):

        print(f"Mammal sound: {self.sound}!")
class Bird(Animal):

    def __init__(self,name,species,age,flight_speed):

        self.flight_speed = flight_speed
        super().__init__(name,species,age)

    def fly(self):

        print(f"{self.name} is flying!")

    def Print(self):
        print(f"Flight speed of {self.name} is: {self.sound}!")

class Reptile(Animal):

    def __init__(self,name,species,age,temperature_preference):

        self.temperature_preference = temperature_preference
        super().__init__(name,species,age)

    def bask(self):

        print(f"{self.name} is basking in the sun.")

    def Print(self):
        print(f"Temperature Preference of {self.name} is: {self.sound}!")


class Herbivore(Animal):

    def __init__(self,name,species,age):

        super().__init__(name,species,age)

    def eat_plants(self):

        print(f"{self.name} is eating plants.")

class Carnivore(Animal):
    
    def __init__(self,name,species,age):
        
        super().__init__(name,species,age)

    def hunt(self):

        print(f"{self.name} is hunting for prey.")

class Omnivore(Herbivore,Carnivore):

    def __init__(self,name,species,age):

        super().__init__(name,species,age)

    def eat_food(self):

        print(f"{self.name} is eating meat as well as plants.")


class Bear(Omnivore):

    def __init__(self,name,species,age,den_location):

        self.den_location = den_location
        super().__init__(name,species,age)

    def hibernate(self):

        print(f"Bear is hibernating in the {self.den_location}!")

    def Print(self):
        print(f"Den_location of {self.name} is: {self.den_location}!")

class Eagle(Bird,Carnivore):

    def __init__(self,name,species,age,flight_speed,nest_location):

        self.nest_location = nest_location
        super().__init__(name,species,age,flight_speed)

    def build_nest(self):

        print(f"{self.name} is building a nest in the {self.nest_location}!")

    def Print(self):
        print(f"Flight speed of {self.name} is {self.flight_speed} and Nest Location is: {self.nest_location}!")

class Python(Reptile):

    def __init__(self, name, species, age, temperature_preference,length):

        self.length = length

        super().__init__(name,species,age,temperature_preference)

    def shed_skin(self):

        print(f"{self.name} is shedding its skin!")

    def Print(self):
        print(f"Length of Python is {self.length} and Temperature Preference is {self.temperature_preference}!")

# zoo class that manage animals in the zoo.

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):

        if isinstance(animal,Animal):

            self.animals.append(animal)

    def list_animals(self):

        for animal in self.animals:
            print(f"Specie: {animal.species} Name: {animal.name} Age:{animal.age}")
            animal.Print()






lion = Bear(name="Leo",species="Bear", age=5,den_location="Cave")
parrot = Eagle(name="Polly",species="Eagle", age=2, flight_speed=30.5, nest_location="Tree")
python = Python(name="Monty",species="Snake/Python", age=3, temperature_preference="Warm", length=3.7)

zoo = Zoo()
zoo.add_animal(lion)
zoo.add_animal(parrot)
zoo.add_animal(python)

# List all animals in the zoo
zoo.list_animals()



print(zoo.animals[0].name)
zoo.animals[0].Print()