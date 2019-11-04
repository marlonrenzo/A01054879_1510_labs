def starting_position():
    coord = {"x": 0, "y": 0}
    return coord


def check_position(position: dict, x_position: int, y_position: int):
    if position["x"] == x_position and position["y"] == y_position:
        return True
    else:
        return False


def show_position(position: dict):
    place_holder = ["[ ]", "[x]"]
    for y_axis in range(5):
        # create the 5 rows
        print("\n")
        for x_axis in range(5):
            # create the 5 columns each row
            # Print the correct place holder within place_holder by the output produced by check_position
            print(place_holder[check_position(position, x_axis, y_axis)], end=" ")
    print("\n")


def get_move():
    move = int(input("Where do you want to move?\n1: up\n2: down\n3: left\n4: right\n"))
    return move


def validate_move(coordinates: dict, direction: int):
    if (coordinates["x"] == 4 and direction == 4) or (coordinates["x"] == 0 and direction == 3):
        return False
    elif (coordinates["y"] == 4 and direction == 2) or (coordinates["y"] == 0 and direction == 1):
        return False
    else:
        return True


def move_character(coordinates: dict, direction: int):
    move = {1: -1, 2: 1, 3: -1, 4: 1}
    if direction == 1 or direction == 2:
        coordinates["y"] += move[direction]
    if direction == 3 or direction == 4:
        coordinates["x"] += move[direction]
    return coordinates


def check_reached_goal(position, at_goal):
    if at_goal:
        show_position(position)
        print("Congratulations! You are a master of this maze!")
    else:
        print("Keep going! I believe in you!")


def game():
    goal = {"x": 4, "y": 4}
    character = starting_position()
    reached_goal = False
    while not reached_goal:
        show_position(character)
        direction = get_move()
        valid_move = validate_move(character, direction)
        if valid_move:
            character = move_character(character, direction)
            reached_goal = check_position(character, goal["x"], goal["y"])
            check_reached_goal(character, reached_goal)
        else:
            print("Cannot go any further, there is a wall there. Try moving in another direction")


if __name__ == "__main__":
    game()
