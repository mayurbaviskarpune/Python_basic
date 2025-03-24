from abc import ABC,abstractmethod

class Vehicle():
    type_vahical = ""     # class variable
    def __init__(self,name="baviskar"):
        self.name = name
        print(self.name)

    def __str__(self):
        print("this is class string")

    @classmethod
    def classfun(cls):
        print(cls.type_vahical)

obj = Vehicle("Marcedes")
obj.type_vahical="nano"
Vehicle.type_vahical = "Marcedes"

Vehicle.classfun()