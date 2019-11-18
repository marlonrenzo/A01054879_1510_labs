_calories = {"lettuce": 5, "carrot": 52, "apple": 72, "bread": 66,"pasta": 221, "rice": 225, "milk": 122, "cheese": 115,"yogurt": 145, "beef": 240, "chicken": 140, "butter": 102}


def get_new_item():
    return input("Enter food item to add, or ’q’ to exit: ")


def calorie_input():# Input loop
    new_item = get_new_item()
    while new_item != "q":
        new_item_calories = int(input("Enter calories for " + new_item + ": "))
        _calories[new_item] = new_item_calories
        total_calories = 0
        for item in _calories:
            total_calories = total_calories + _calories[item]

        food_item_names = []
        for item in _calories:
            food_item_names.append(item)
        avg_calories = total_calories / len(_calories)



        print("\nFood Items:", sorted(food_item_names))
        print("Total Calories:", total_calories,"Average Calories: %0.1f\n" % avg_calories)

        new_item = get_new_item()


def main():
    something()


if __name__ == '__main__':
    main()
