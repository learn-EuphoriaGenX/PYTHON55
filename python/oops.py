class Blueprint:

    def __init__(self, name, floor, room): # constructor method
        self.name = name
        self.floor = floor
        self.room = room


house1 = Blueprint( "Arman Villa", 3, 6) # object instantiate
house2 = Blueprint( "Ghatka Apartment", 2, 10) # object instantiate

print(f'House name is {house1.name}, Floor is {house1.floor}, Available rooms {house1.room}')
print(f'House name is {house2.name}, Floor is {house2.floor}, Available rooms {house2.room}')


class Car:
    def __init__(self, name, year, color, type, seater):
        self.name = name
        self.brand = "Honda"
        self.year = year
        self.color = color
        self.type = type
        self.seater = seater

    def move_forward(self):
        print(f'{self.name} from {self.brand} moving forward.')
    def move_backward(self):
        print(f'{self.name} from {self.brand} moving backward.')
    def drift_maro(self):
        print(f'{self.name} from {self.brand} drift mar rahe hai.')

        
car1 = Car("Civic",  2014, "Blue", "sedan", 5)
car2 = Car("Amaze",  2015, "Black", "sedan", 4)
car3 = Car("Elevate",  2020, "White", "SUV", 6)
car4 = Car("City Hybrid",  2023, "Red", "seadan", 5)
car5 = Car("eHEV",  2025, "Blue", "Green", 6)


cars = [car1, car2, car3, car4, car5]
for i in range(0, len(cars)):
    cars[i].move_forward()
    cars[i].move_backward()
    cars[i].drift_maro()
    print("\n")


