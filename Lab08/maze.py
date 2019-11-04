def starting_position():
    """
    Return the starting position.

    :return: a dictionary
    """
    coord = {"x": 0, "y": 0}
    return coord


def check_position(position: dict, x_position: int, y_position: int):
    """
    Check if position provided is located at the same position as the provided x and y coordinates.

    :param position: a dictionary
    :param x_position: an int
    :param y_position: an int
    :precondition: position must be a dictionary with x and y
    :precondition: x_position and y_position must be integers
    :post condition: will return the equality of the two coordinates as a boolean
    :return: a boolean
    """
    if position["x"] == x_position and position["y"] == y_position:
        return True
    else:
        return False


def show_position(position: dict):
    """
    Show the current position of the character.

    :param position: a dictionary
    :precondition: position must be a dictionary with x and y coordinates
    :post condition: will print the 5x5 grid and show where the character is located at.
    """
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
    """
    Ask the user for the direction of a move.

    :return: an int
    """
    move = int(input("Where do you want to move?\n1: up\n2: down\n3: left\n4: right\n"))
    return move


def validate_move(coordinates: dict, direction: int):
    """
    Validate that the move will be within the 5x5 limits.

    :param coordinates: a dictionary
    :param direction: an int
    :precondition: coordinates must be a dictionary with x and y coordinates
    :precondition: direction must be an integer between 1 - 4 inclusive
    :post condition: will return the validity of the move as a boolean
    :return: a boolean
    """
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
