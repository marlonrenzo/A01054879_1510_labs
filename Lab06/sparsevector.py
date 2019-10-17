def sparse_add(vector_one, vector_two):
    vector_sum = {}
    for key in vector_one.keys():
        if key not in vector_one.keys():
            vector_sum[key] = vector_two[key]
        elif key not in vector_two.keys():
            vector_sum[key] = vector_one[key]
        else:
            vector_sum[key] = vector_one[key] + vector_two[key]

    for key in vector_two.keys():
        if key not in vector_one.keys():
            vector_sum[key] = vector_two[key]
        elif key not in vector_two.keys():
            vector_sum[key] = vector_one[key]
        else:
            vector_sum[key] = vector_one[key] + vector_two[key]

    return vector_sum


def main():
    print(sparse_add({0: 1, 3: 4, 6: 5}, {2: 1, 4: 7, 10: 4}))


if __name__ == "__main__":
    main()

