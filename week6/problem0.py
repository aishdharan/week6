import sys


# Find sum of numbers in a list


def sum_of_list(list, size):
    # size = len(list)
    # return list[size - 1] + sum_of_list(list, size - 1)

    # total_list = sum_of_list(list1, len(list1))
    # print(f"Sum of all elements in a given list= {total_list}")

    # total_list = sum_of_list(list, size)
    if size == 0:
        return 0
    else:
        return list[size - 1] + sum_of_list(list, size - 1)


def main():
    list1 = [2, 4, 5, 6, 8, 9]
    total_list = sum_of_list(list1, len(list1))
    print(f"Sum of all elements in a given list= {total_list}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

