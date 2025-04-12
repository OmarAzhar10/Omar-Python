# class Animal():
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
        
#     def speak(self):
#         print(f"{self.name} is speaking")

#     def walk(self):
#         print(f"{self.name} is walking")


# class Dog(Animal):
#     def __init__(self, name, color):
#         super().__init__(name, color)

#     def speak(self):
#         print(f"{self.name} is barking")

# dog1 = Dog("Buddy", "Light brown")
# dog1.speak()
# dog1.walk()                        



from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class car(Vehicle):
    def start_engine(self):
        print("Car engine started. Vrooooooooooooooooom!")
    def horn(self):
        print("Beeeeeeeeeeeeeeep!!")


class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started. Zooooooooooooooooom!")


carObj = car()
carObj.start_engine()
carObj.horn()
bikeObj = Bike()
bikeObj.start_engine()
    