def base_conversion():
    """
    Convert a base 10 number to base n
    :postcondition: convert input to destination base.
    :return: base-n number
    """

    desired_base = int(input("Enter your destination base between 2 to 9:\n"))
    maximum_base_10 = 2 ** desired_base - 1
    maximum_base_10 = str(maximum_base_10)
    Base_10 = int(input(f"Enter a Base 10 number less than or equal to {maximum_base_10}:\n"))


    right_most = str(Base_10 % desired_base)
    base_10 = int(Base_10 / desired_base)
    right_middle = str(base_10 % desired_base)
    base_10 = int(base_10 / desired_base)
    left_middle = str(base_10 % desired_base)
    base_10 = int(base_10 / desired_base)
    left_most = str(base_10 % desired_base)
    conversion = int(left_most + left_middle + right_middle + right_most)
    conversion_phrase = (f"{Base_10} base 10 converted to base {desired_base} is: {conversion}")

    return conversion_phrase