def get_input_destination_base():
    """
    Acquire the destination base from the user.

    :return: destination base as an int
    """
    input_destination_base = int(input("Enter your destination base between 2 to 9:\n"))
    return input_destination_base


def get_input_base_10(desired_base):
    """
    Acquire the base 10 number to convert from the user.

    :return:
    """
    maximum_base_10 = get_maximum_base(desired_base)
    base_10 = int(input(f"Enter a Base 10 number less than or equal to {maximum_base_10}:\n"))
    return base_10


def get_maximum_base(desired_base):
    """
    Determine the maximum base 10 number the user can input.

    :param desired_base: input from user as an int
    :return: maximum number in base 10
    """
    maximum_base_10 = 2 ** desired_base - 1
    maximum_base_10 = str(maximum_base_10)
    return maximum_base_10


def convert(user_input, user_destination):
    """
    Convert a base 10 number into base n.

    :param user_input: int
    :param user_destination: int
    :postcondition: convert input to destination base.
    :return: a converted integer
    """
    right_most = str(get_digit(user_input,user_destination,0))
    right_middle = str(get_digit(user_input,user_destination,1))
    left_middle = str(get_digit(user_input,user_destination,2))
    left_most = str(get_digit(user_input,user_destination,3))
    conversion = int(left_most + left_middle + right_middle + right_most)
    return conversion


def get_digit(dividend, divisor, number_of_digits_from_right):

    digit = int(dividend / (divisor ** number_of_digits_from_right) % divisor)

    return digit




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
    Base_10 = get_input_base_10(desired_base)
    conversion = convert(Base_10, desired_base)
    print(format_conversion(Base_10, desired_base, conversion))


if __name__ == '__main__':
    base_conversion()

