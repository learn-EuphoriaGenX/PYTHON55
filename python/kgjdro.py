import random
def roll_dice(color):
    print(f"rolling for {color} ... ")
    random_value = random.randint(1, 6)
    print(".....")
    return random_value

a = roll_dice("black")
print(+50)