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
    roll = random.randint(number_of_rolls, number_of_sides * number_of_rolls)
    return roll


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
        return 0
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
    Return
    :precondition: the function will only work for positive non-zero integers
    :postcondition:
    :param syllables: an integer
    :return:
    """
    pass

def generate_vowel():
    """

    :return:
    """


def create_character(name_length):
    """

    :param name_length: an integer
    :return:
    """
    pass


def print_character(character):
    """

    :param character: a list
    :return:
    """
    pass


def main():
    """

    :return:
    """
    inventory = ['Longsword','Dagger','Bow','Staff','Wand','Shield','Spear','Axe','Hammer']
    print(choose_inventory(inventory,2))
    doctest.testmod()

if __name__ == '__main__':
    main()