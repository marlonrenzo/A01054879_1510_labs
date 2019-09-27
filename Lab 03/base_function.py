import doctest


def convert(user_input, user_destination):
    """
    Convert a base 10 number into base n.

    :precondition: both numbers must be positive integers.
    :param user_input: int
    :param user_destination: int
    :postcondition: convert input to destination base.
    :return: a converted integer

    >>> convert(6560, 9)
    8888
    >>> convert(1, 9)
    1
    >>> convert(1897, 9)
    2537
    """
    right_most = str(get_digit(user_input,user_destination,0))
    right_middle = str(get_digit(user_input,user_destination,1))
    left_middle = str(get_digit(user_input,user_destination,2))
    left_most = str(get_digit(user_input,user_destination,3))
    conversion = int(left_most + left_middle + right_middle + right_most)
    return conversion


def get_digit(dividend, divisor, number_of_digits_from_right):
    """
    Calculate a digit by finding the remainder between the dividend and the divisor.

    :precondition: both numbers must be positive integers.
    :param dividend: base 10 number as a postive int less than n^4 - 1
    :param divisor: destination base as a postive int between 2 and 9
    :param number_of_digits_from_right: character place from right as an int
    :return: the digit as an int

    >>> get_digit(45, 7, 1)
    6
    >>> get_digit(6560, 9, 0)
    8
    >>> get_digit(4095, 8, 0)
    7

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

    >>> format_conversion(150,20,7654)
    '150 base 10 converted to base 20 is: 7654'
    >>> format_conversion(-150,-20,-7654)
    '-150 base 10 converted to base -20 is: -7654'
    >>> format_conversion(0,0,0)
    '0 base 10 converted to base 0 is: 0'
    """
    conversion_phrase = (f"{base_10} base 10 converted to base {desired_base} is: {conversion}")

    return conversion_phrase


def base_conversion(desired_base, base_10):
    """
    Convert a base 10 number to base n.

    Act as the main and call all required functions to complete the conversion.
    :precondition: desired_base should be a positive integer in between 2 and 9
    :precondition: base_10 has to below n^4 - 1
    :postcondition: convert input to destination base.
    :return: converted base-n string

    >>> base_conversion(8, 4095)
    4095 base 10 converted to base 8 is: 7777
    >>> base_conversion(8, 1)
    1 base 10 converted to base 8 is: 1
    >>> base_conversion(8, 1287)
    1287 base 10 converted to base 8 is: 2407
    """

    conversion = convert(base_10, desired_base)
    print(format_conversion(base_10, desired_base, conversion))


def main():
    """
    Invoke function to run program.
    """
    doctest.testmod()
    base_conversion(7, 30)
    base_conversion(9, 255)
    base_conversion(3, 10)


if __name__ == '__main__':
    main()

