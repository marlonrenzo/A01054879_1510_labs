import random

def roll_die(number_of_rolls,number_of_sides):
    """
    Provide random integers based on the parameters.

    :precondition: the parameters must be postive integers
    :param number_of_rolls: an int
    :param number_of_sides: an int
    :return: the total of the rolls as an int
    """
    if number_of_rolls < 1 or number_of_sides < 1:
        return 0

    elif number_of_rolls == 1:
        roll_one = random.randint(1, number_of_sides)
        sum = roll_one
        return sum

    elif number_of_rolls == 2:
        roll_one = random.randint(1, number_of_sides)
        roll_two = random.randint(1, number_of_sides)
        sum = roll_one + roll_two
        return sum

    elif number_of_rolls == 3:
        roll_one = random.randint(1, number_of_sides)
        roll_two = random.randint(1, number_of_sides)
        roll_three = random.randint(1, number_of_sides)
        sum = roll_one + roll_two + roll_three
        return sum



def create_name(length):
    """
    Generate a random string with a length depending on the parameter.

    :precondition: length must be a positive integer.
    :param length:
    :return:
    """
    letters = "abcdefghijklmnopqrstuvwxyz"

    if length < 1:
      return None

    elif length == 1:
        letter_one = random.choice(letters)
        name = letter_one
        return name
    elif length == 2:
        letter_one = random.choice(letters)
        letter_two = random.choice(letters)
        name = letter_one + letter_two
        return name
    elif length == 3:
        letter_one = random.choice(letters)
        letter_two = random.choice(letters)
        letter_three = random.choice(letters)
        name = letter_one + letter_two + letter_three
        name = name.capitalize()
        return name

    elif length == 4:
        letter_one = random.choice(letters)
        letter_two = random.choice(letters)
        letter_three = random.choice(letters)
        letter_four = random.choice(letters)
        name = letter_one + letter_two + letter_three + letter_four
        return name

    elif length == 5:
        letter_one = random.choice(letters)
        letter_two = random.choice(letters)
        letter_three = random.choice(letters)
        letter_four = random.choice(letters)
        letter_five = random.choice(letters)
        name = letter_one + letter_two + letter_three + letter_four + letter_five
        name = name.capitalize()
        return name


def main():
    """
    Test the functions.
    :return:
    """
    print(roll_die(0, 6))
    print(roll_die(3, 12))
    print(roll_die(2, 5))

    print(create_name(3))
    print(create_name(5))
    print(create_name(0))


if __name__ == '__main__':
    main()

