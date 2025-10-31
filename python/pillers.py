# Inheritance ✅

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal): # subclass, inheritance, child class, derived class
    def speak(self): # method overriding
        print(f"{self.name} barks.")


class SastaCalculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b
    
class AdvancedCalculator(SastaCalculator): # inheritance
    def __init__(self, a, b, c):
        # self.a = a
        # self.b = b
        super().__init__(a, b)  # calling parent class constructor
        self.c = c

    def add(self):  # method overriding
        return self.a + self.b + self.c

    def multiply(self):
        return self.a * self.b * self.c

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Cannot divide by zero"

# calc1 = SastaCalculator(10, 5)
# print(calc1.add())
# print(calc1.subtract())

# calc2 = AdvancedCalculator(20, 4, 2)
# print(calc2.add())          # inherited method
# print(calc2.subtract())     # inherited method
# print(calc2.multiply())     # new method
# print(calc2.divide())       # new method


# Polymorphism ✅
class Vehicle:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    # def moving(self):
    #     pass

    def moving(self):
        print("Vehicle is moving")

class Boat(Vehicle):
    def moving(self):
        print(f"{self.name} the {self.type} boat is sailing.")

class Airplane(Vehicle):
    def moving(self):
        print(f"{self.name} the {self.type} airplane is flying.")

class Car(Vehicle):
    def moving(self):
        print(f"{self.name} the {self.type} car is driving.")

vehicle1 = Vehicle("Vehicle", "type")
boat1 = Boat("Sea Explorer", "Yacht") # object of Boat class
airplane1 = Airplane("Sky High", "Jet") # object of Airplane class
car1 = Car("Road Runner", "Sedan") # object of Car class

for vehicle in (vehicle1, boat1, airplane1, car1):
    vehicle.moving()
