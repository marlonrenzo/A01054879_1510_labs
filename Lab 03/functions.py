import random

def roll_die(number_of_rolls,number_of_sides):
    if number_of_rolls == 1:
        roll_one = random.randint(1, number_of_sides)
        sum = roll_one
        return sum

    elif number_of_rolls == 2:
        roll_one = random.randint(1, number_of_sides)
        roll_two = random.randint(1, number_of_sides)
        sum = str(roll_one) + str(roll_two)
        return sum

    elif number_of_rolls == 3:
        roll_one = random.randint(1, number_of_sides)
        roll_two = random.randint(1, number_of_sides)
        roll_three = random.randint(1, number_of_sides)
        sum = str(roll_one) + str(roll_two) + str(roll_three)
        return sum

    elif number_of_rolls == 0 or number_of:
        print(0)


roll_die(0,6)
