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
    for i in integers:
        if i % number == 0:
            multiples += 1
    return multiples


def prepender(strings, added_string):
    """

    :param strings:
    :param added_string:
    :precondition: strings must be a list of strings
    :precondition: added_string must be a string
    :post condition: will return a list with added_string added to each of the original list
    :return:
    """
    for index in range(len(strings)):
        strings[index] = added_string + strings[index]
    return strings


def main():
    doctest.testmod()
    # print(list_tagger([1, 234, 56, 7]))
    print(cutoff([1, 3, 6, 9], 3))


if __name__ == "__main__":
    main()
