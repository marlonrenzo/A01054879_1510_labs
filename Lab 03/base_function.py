def get_input_destination_base():
    """
    Acquire the destination base from the user.

    :return: destination base as an int between 2 and 9
    """
    input_destination_base = int(input("Enter your destination base between 2 to 9:\n"))
    return input_destination_base


def get_input_base_10(desired_base):
    """
    Acquire the base 10 number to convert from the user.
    :param: destination base as an int between 2 and 9
    :return: the input from user as postive int less than maximum_base_10
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
    """
    Calculate the digit by finding the remainder between the dividend and the divisor.

    :param dividend: base 10 number as a postive int less than maximum_base_10
    :param divisor: destination base as a postive int between 2 and 9
    :param number_of_digits_from_right: character place from right as an int
    :return: the digit as an int
    """
    digit = int(dividend / (divisor ** number_of_digits_from_right) % divisor)

    return digit


def format_conversion(base_10,desired_base,conversion):
    """
    Print a string showing the determined conversion.

    :param base_10: base 10 number as a postive int less than maximum_base_10
    :param desired_base: destination base as a postive int between 2 and 9
    :param conversion: the final converted base n int
    :return: a string containing the data collected.
    """
    conversion_phrase = (f"{base_10} base 10 converted to base {desired_base} is: {conversion}")

    return conversion_phrase


def base_conversion():
    """
    Convert a base 10 number to base n.

    Act as the main and call all required functions to complete the conversion.

    :postcondition: convert input to destination base.
    :return: base-n number
    """

    desired_base = get_input_destination_base()
    Base_10 = get_input_base_10(desired_base)
    conversion = convert(Base_10, desired_base)
    print(format_conversion(Base_10, desired_base, conversion))


if __name__ == '__main__':
    base_conversion()

