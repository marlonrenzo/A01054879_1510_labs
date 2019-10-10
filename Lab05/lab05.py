import random
import doctest


def roll_die(number_of_rolls, number_of_sides):
    """
    Will return a random positive integer base on the parameters.

    :precondition: both parameters must be positive.
    :param number_of_rolls: an integer determining how many times to roll the die
    :param number_of_sides: an integer determining the upper bound of one roll
    :return: a random integer containing the sum of all rolls performed
    """
    total = 0
    for x in range(0, number_of_rolls):
        roll = random.randint(1, number_of_sides)
        total = total + roll
    return total


def choose_inventory(inventory, selection):
    """
    Select items from inventory and place into a sorted list.

    Check all cases ranging from empty lists, 0 selections or negative selections and print a warning for these cases.

    :precondition: selection must be a positive integer less than or equal to the length of inventory
    :precondition: inventory must not be an empty list
    :postcondition: a sorted list with selected items, the length of the list depends on the value of selections
    :param inventory: a list with items to select from
    :param selection: an integer for the number of selections from the list
    :return: a sorted list
    >>> choose_inventory([],0)
    0
    >>> choose_inventory(['One'],-1)
    Warning: Your selection of items for inventory items is a negative number.
    []
    >>> choose_inventory(['first','second','third'],4)
    Warning: Your Selection of items for inventory items is a larger than the amount items available.
    ['first', 'second', 'third']
    """
    if inventory == [] and selection == 0:
        return []
    elif selection < 0:
        print("Warning: Your selection of items for inventory items is a negative number.")
        return []
    elif selection > (len(inventory)):
        print("Warning: Your Selection of items for inventory items is a larger than the amount items available.")
        sorted_inventory = sorted(inventory)
        return sorted_inventory
    else:
        random_selection = random.sample(inventory, selection)
        random_selection.sort()
        return random_selection


def generate_name(syllables):
    """
    Generate a name base on a given amount of syllables.

    :precondition: the function will only work for positive non-zero integers
    :postcondition: return a string of letters alternating vowels and consonants
    :param syllables: an integer
    :return: a concatenated string of random letters
    """
    string = ""
    for x in range(0, syllables):
        string = string + generate_syllable()
    return string.capitalize()


def generate_vowel():
    """
    Generate a random vowel.
    :return: a random vowel character
    """
    vowel = ['a', 'e', 'i', 'o', 'u', 'y']
    random_selection = random.choice(vowel)
    return random_selection


def generate_consonant():
    """
    Generate a random consonant.
    :return: a random consonant character
    """
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    random_selection = random.choice(consonant)
    return random_selection


def generate_syllable():
    """
    Generate a random syllable.
    :return: a random syllable as a concatenated string
    """
    vowel = generate_vowel()
    consonant = generate_consonant()
    syllable = vowel + consonant
    return syllable



def create_character(name_length):
    """
    Create a list including items to associate to a character.

    Each list element, except for the character name, will be a mini list containing an attribute along with a value.
    :param name_length: an integer
    :return:
    """
    character = [generate_name(name_length // 2), ['Strength', roll_die(3, 6)],
                 ['Dexterity', roll_die(3, 6)],['Constitution', roll_die(3, 6)],
                 ['Intelligence', roll_die(3, 6)], ['Wisdom', roll_die(3, 6)],
                 ['Charisma', roll_die(3, 6)]]
    return character


def print_character(character):
    """
    Format character's attributes in a neat and legible way.

    Pop each element one after the other, and print the attribute name along with value.
    :param character: a list with all character attributes
    :return: formatted string with all character attributes
    """
    print(f"Name: {character[0]}")
    attribute_one = character.pop(1)
    print(f"{attribute_one[0]}: {attribute_one[1]}")
    attribute_two = character.pop(1)
    print(f"{attribute_two[0]}: {attribute_two[1]}")
    attribute_three = character.pop(1)
    print(f"{attribute_three[0]}: {attribute_three[1]}")
    attribute_four = character.pop(1)
    print(f"{attribute_four[0]}: {attribute_four[1]}")
    attribute_five = character.pop(1)
    print(f"{attribute_five[0]}: {attribute_five[1]}")
    attribute_six = character.pop(1)
    print(f"{attribute_six[0]}: {attribute_six[1]}")


def main():
    """
    Call all functions to run the program.
    """
    # inventory = ['Longsword', 'Dagger', 'Bow', 'Staff', 'Wand', 'Shield', 'Spear', 'Axe', 'Hammer']
    # print(choose_inventory(inventory,2))
    # print(generate_vowel())
    # doctest.testmod()
    # print(generate_name(4))
    # print(roll_die(3,6))
    # print(create_character(8))
    print_character(create_character(8))


if __name__ == '__main__':
    main()
