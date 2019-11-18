import doctest


def print_result(items: list, total: int, average: float) -> None:
    """
    Print the final result including the items, total calories and average calories.

    :param items: a list
    :param total: an int
    :param average: a float
    :precondition: items must be a list with homogeneous data types
    :precondition: total must be a positive int
    :precondition: average must be a positive float
    :post condition: will print all values in an informing way
    :return: None

    >>> print_result([1, 2], 3, 4.0)
    <BLANKLINE>
    Food Items: [1, 2]
    Total Calories: 3 Average Calories: 4.0
    <BLANKLINE>
    >>> print_result(['food', 'morefood', 'just fat'], 99, 456.5)
    <BLANKLINE>
    Food Items: ['food', 'just fat', 'morefood']
    Total Calories: 99 Average Calories: 456.5
    <BLANKLINE>
    """
    print("\nFood Items:", sorted(items))
    print("Total Calories:", total, "Average Calories: %0.1f\n" % average)


def get_food_items() -> dict:
    """
    Provide a dictionary with food items and their caloric value.

    :return: a dict

    """
    return {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66, "pasta": 221, "rice": 225, "milk": 122, "cheese": 115,
            "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102}


def calorie_calculator() -> None:  # Input loop
    """
    Calculate the average and total calories of food items.

    Create a dictionary with food items as keys and their respective caloric value.

    Acquire a new item from user, append it to the collection of items and calculate the new average and total calories.

    :return: None

    """
    _calories = get_food_items()
    new_item = input("Enter food item to add, or ’q’ to exit: ")
    while new_item != "q":
        _calories[new_item] = int(input("Enter calories for " + new_item + ": "))
        total_calories = sum(_calories.values())
        food_item_names = list(_calories.keys())
        avg_calories = total_calories / len(_calories)
        print_result(food_item_names, total_calories, avg_calories)

        new_item = input("Enter food item to add, or ’q’ to exit: ")


def main():
    doctest.testmod()
    calorie_calculator()


if __name__ == '__main__':
    main()
