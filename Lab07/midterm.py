import doctest
import random


def list_tagger(batch):
    """
    Tag a list with its length as an int at the beginning of the list.

    :param batch: a list
    :precondition: batch must be a list
    :post condition: will return a tagged list
    :return: a list
    >>> list_tagger([])
    [0]
    >>> list_tagger([123456789])
    [1, 123456789]
    >>> list_tagger([1, 2, 3, 4, 5])
    [5, 1, 2, 3, 4, 5]
    """
    length = len(batch)
    batch.insert(0, length)
    return batch


def cutoff(integers, number):
    """
    Determine the amount of multiples in a given list based on the number provided.

    :param integers: a list
    :param number: an int
    :precondition: integers must be a list with int numbers
    :post condition: will return an integer that represents the amount of multiples in a list
    :return: an int
    >>> cutoff([1, 3, 6, 9], 3)
    3
    >>> cutoff([1, 4, 6, 8, 14], 2)
    4
    """
    multiples = 0
    if number == 0:
        return 0
    else:
        for i in integers:
            if i % number == 0:
                multiples += 1
        return multiples


def prepender(strings, added_string):
    """
    Append a string to the beginning of all strings in a list.

    :param strings: a list
    :param added_string: a string
    :precondition: strings must be a list of strings
    :precondition: added_string must be a string
    :post condition: will return a list with added_string appended to the beginning of each string
    :return: a list
    >>> prepender(['hi', 'hey', 'hello'], 'YO')
    ['YOhi', 'YOhey', 'YOhello']
    >>> prepender(['smith', 'appleseed', 'thompson'], 'Mr. ')
    ['Mr. smith', 'Mr. appleseed', 'Mr. thompson']
    """
    for index in range(len(strings)):
        strings[index] = added_string + strings[index]
    return strings


def name_list():
    """
    Create a dictionary of names provided by a user, corresponding each string to their length.

    :return: a dictionary
    """
    names = {}
    while True:
        user_input = input("Enter a name. ('quit' to finish)")
        if user_input.lower() == 'quit':
            break
        elif len(user_input) not in names:
            names[len(user_input)].append(user_input)
        else:
            names[len(user_input)] = [user_input]
    return names


def multiples_of_3(upper_bound):
    """
    Add the sum of all multiples of three under the upper_bound.

    :param upper_bound: an int
    :precondition: parameter must be a positive integer
    :post condition: will return the sum of all multiples of three under the upper_bound
    :return: an int
    >>> multiples_of_3(10)
    18
    """
    multiple_sum = 0
    for multiple in range(3, upper_bound, 3):
        multiple_sum += multiple
    return multiple_sum


def roll_counter():
    """
    Roll a user-specified sided die a user-specified amount of times and count the times a number is rolled.

    :return: a dictionary
    """
    number_of_sides = int(input("Enter the size of the die you would like to roll. \n"))
    number_of_rolls = int(input("Enter the amount of times you would like to roll. \n"))
    roll_tally = {i + 1 : 0 for i in range(number_of_sides)}
    while number_of_rolls > 0:
        number_of_rolls -= 1
        roll_tally[random.randint(1, number_of_sides)] += 1
    return roll_tally


def print_dictionary(dictionary):
    """
    Print the keys and their values of a dictionary into a legible way.

    :param dictionary: a dictionary
    :precondition: parameter must be a dictionary
    :post condition: will print all keys and their values
    """
    for key in dictionary.keys():
        print(f"{key} : {dictionary[key]}")


def main():
    doctest.testmod()
    print(list_tagger([1, 2, 3, 4, 5]))
    print(cutoff([1, 4, 6, 8, 14], 2))
    print(name_list())
    print(multiples_of_3(25))
    print(prepender(['smith', 'appleseed', 'thompson'], 'Mr. '))
    print_dictionary(roll_counter())



if __name__ == "__main__":
    main()
