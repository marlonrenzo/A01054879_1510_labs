def main():
    """
    Create some errors
    :return: chaos
    """

    ZeroDivisionError = 5 / 0
    print(ZeroDivisionError)
    
    index_error_one = "123456789"
    print(index_error_one[-10])

    index_error_two = "chris is pretty cool"
    print(index_error_two[20])

    string_one = "ten"
    string_two = "five"
    type_error_one = string_one / string_two
    print(type_error)

    number = 123456789
    type_error_two = len(number)
    print(number_length)


if __name__ == '__main__':
    main()