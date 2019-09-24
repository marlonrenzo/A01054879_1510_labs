def get_input_destination_base():
    """
    Acquire input from the user.
    :return: destination base as an int
    """
    input_destination_base = int(input("Enter your destination base between 2 to 9:\n"))
    return input_destination_base
#
#
# def get_input_base_10(maximum_base_10):
#     """
#     Acquire input from the user.
#     :return:
#     """
#     base_10 = int(input(f"Enter a Base 10 number less than or equal to {maximum_base_10}:\n"))
#
#
def convert(user_input, user_destination):
    """
    Convert a base 10 number into base n.
    :param user_input: int
    :param user_destination: int
    :postcondition: convert input to destination base.
    :return: a converted integer
    """
    right_most = str(user_input % user_destination)
    base_10 = int(user_input / user_destination)
    right_middle = str(base_10 % user_destination)
    base_10 = int(base_10 / user_destination)
    left_middle = str(base_10 % user_destination)
    base_10 = int(base_10 / user_destination)
    left_most = str(base_10 % user_destination)
    conversion = int(left_most + left_middle + right_middle + right_most)
    return conversion
#
#
# def find_remainder():
#     """
#     Determine the remainder between two numbers.
#     :return: remainder as an int
#     """
#     right_most = str(user_input % user_destination)
#
#
# def operation():
#     """
#
#     :return:
#     """
#
#
def format_conversion(base_10,desired_base,conversion):
    """
    Print a string showing the determined conversion.
    :param Base_10: int
    :param desired_base: int
    :param conversion: string
    :return: a string containing the data collected.
    """
    conversion_phrase = (f"{base_10} base 10 converted to base {desired_base} is: {conversion}")

    return conversion_phrase


def base_conversion():
    """
    Convert a base 10 number to base n
    :postcondition: convert input to destination base.
    :return: base-n number
    """

    desired_base = get_input_destination_base()
    maximum_base_10 = 2 ** desired_base - 1
    maximum_base_10 = str(maximum_base_10)
    Base_10 = int(input(f"Enter a Base 10 number less than or equal to {maximum_base_10}:\n"))

    conversion = convert(Base_10, desired_base)
    print(format_conversion(Base_10, desired_base, conversion))


if __name__ == '__main__':
    base_conversion()

