def print_result(items, total, average):
    print("\nFood Items:", sorted(items))
    print("Total Calories:", total, "Average Calories: %0.1f\n" % average)


def calorie_calculator(_calories):  # Input loop
    new_item = input("Enter food item to add, or ’q’ to exit: ")
    while new_item != "q":
        _calories[new_item] = int(input("Enter calories for " + new_item + ": "))
        total_calories = sum(_calories.values())
        food_item_names = list(_calories.keys())
        avg_calories = total_calories / len(_calories)
        print_result(food_item_names, total_calories, avg_calories)

        new_item = input("Enter food item to add, or ’q’ to exit: ")


def main():
    _calories = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66, "pasta": 221, "rice": 225, "milk": 122,
                 "cheese": 115,
                 "yogurt": 145, "beef": 240, "chicken": 140, "butter": 102}
    calorie_calculator(_calories)


if __name__ == '__main__':
    main()
