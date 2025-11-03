from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("wof wof!")
    
class Lion(Animal):
    def make_sound(self):
        print("lion make sound")



dog1 = Dog()
dog1.make_sound()
lion1 = Lion()
lion1.make_sound()