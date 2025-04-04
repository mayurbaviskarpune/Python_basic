# from abc import ABC,abstractmethod

# class Vehicle():
#     type_vahical = ""     # class variable
#     def __init__(self,name="baviskar"):
#         self.name = name
#         print(self.name)

#     def __str__(self):
#         print("this is class string")

#     @classmethod
#     def classfun(cls):
#         print(cls.type_vahical)

#     @abstractmethod
#     def fun2(self):
#         pass


# obj = Vehicle("Marcedes")
# obj.type_vahical="nano"
# Vehicle.type_vahical = "Marcedes"

# Vehicle.classfun()


#########################################################
from abc import ABC, abstractmethod

# Abstract Base Class
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass  # No implementation

    @abstractmethod
    def stop_engine(self):
        pass  # No implementation

    @abstractmethod
    def drive(self):
        pass  # No implementation

# Subclass (Must Implement All Abstract Methods)
class Car(Vehicle):

    def start_engine(self):
        return "Car engine started."

    def stop_engine(self):
        return "Car engine stopped."

    def drive(self):
        return "Car is driving."

# Subclass for Bike
class Bike(Vehicle):

    def start_engine(self):
        return "Bike engine started."

    def stop_engine(self):
        return "Bike engine stopped."

    def drive(self):
        return "Bike is driving."

# Creating objects
car = Car()
print(car.start_engine())  # Output: Car engine started.
print(car.drive())         # Output: Car is driving.
print(car.stop_engine())   # Output: Car engine stopped.

bike = Bike()
print(bike.start_engine())  # Output: Bike engine started.
print(bike.drive())         # Output: Bike is driving.
print(bike.stop_engine())   # Output: Bike engine stopped.

# Trying to instantiate Vehicle directly will cause an error:
# vehicle = Vehicle()  # TypeError: Can't instantiate abstract class
