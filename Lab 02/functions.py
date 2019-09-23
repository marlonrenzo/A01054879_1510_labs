def format_name(first_name,last_name):
    """
    Return a formatted full name.

    Take a user's first and last name to format it by stripping the white space and capitalizing the first letters.

    :param first_name: string
    :param last_name: string
    :postcondition: concatenate and format input
    :return: a concatenated string

    """

    strip_first_name = first_name.strip()
    first_name_final = strip_first_name.capitalize()
    strip_last_name = last_name.strip()
    last_name_final = strip_last_name.capitalize()
    full_name = first_name_final + " " + last_name_final

    return(full_name)


def name_input():
    """
    Acquire first and last name from user.

    :return: a final formatted string
    """
    user_first_name = input("Please enter your first name:\n")
    user_last_name = input("Please enter your last name:\n")
    return format_name(user_first_name, user_last_name)


def tripler(input):
    """
    Return a tripled input.

    :param input: any
    :return: a string repeated 3 times
    """

    input = str(input) * 3
    return input


def this_year():
    """
    Return the current year.

    Goes through a series of operations that outputs 2019.

    :return: 2019 as an int
    """

    year = 3
    year_2 = 0.1661060837
    year = (year * year * year - year) + year_2
    number = 100 - year
    year = (number / 6) * (number / 6) * (number / 6) + 0.9878948
    year = int(year)
    return year


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


def main():
    """
    Invoke all functions.

    Test the functions in this module.
    """


    # print(name_input())
    print(format_name("marlon","fajardo"))
    print(format_name("MARLON","FAJARDO"))
    print(format_name("     marlon    ","        fajardo      "))
    #End of format_name function test

    # object = input("Enter any type of value to be tripled:\n")
    print(tripler("christhompson1510"))
    print(tripler("bcit_!@#$%^&*"))
    print(tripler(3.14159))
    #End of tripler function test


    print("The year is:",this_year())
    #End if year function test

    print(base_conversion())
    #End of base_conversion test


if __name__ == '__main__':
    main()

