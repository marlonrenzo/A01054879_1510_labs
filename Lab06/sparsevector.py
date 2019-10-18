def sparse_add(vector_one, vector_two):
    """
    Add the common key values of two dictionaries and store the sum in a new dictionary.

    :param vector_one: dictionary with integers
    :param vector_two: dictionary with integers
    :return: a dictionary with all common vectors added
    """
    vector_sum = {}
    for key in vector_one.keys():
        if key not in vector_two.keys():
            vector_sum[key] = vector_one[key]
        else:
            vector_sum[key] = vector_one[key] + vector_two[key]

    for key in vector_two.keys():
        if key not in vector_one.keys():
            vector_sum[key] = vector_two[key]
    for key in vector_sum:
        if vector_sum[key] == 0:
            del vector_sum[key]
    return vector_sum


def main():
    print(sparse_add({0: 1, 3: 4, 6: 5}, {2: 1, 4: 7, 10: 4}))


if __name__ == "__main__":
    main()

