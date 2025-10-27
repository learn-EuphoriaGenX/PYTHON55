import random
def roll_dice(color):
    print(f"rolling for {color} ... ")
    random_value = random.randint(1, 6)
    return random_value

win_point = int(input("Point: "))
green_total = 0
red_total = 0

while True:
    green_input = input("Roll Dice for Green: ")
    green_curr_value = roll_dice("Green")
    green_total += green_curr_value

    red_input = input("Roll Dice for Red: ")
    red_curr_value = roll_dice("Red")
    red_total += red_curr_value

    print(f'Green: {green_total} | Red: {red_total}')

    if green_total >= win_point:
        print("******GREEN WIN*****")
        break
    if red_total >= win_point:
        print("******RED WIN*****")
        break
 


