import sys


# Find sum of numbers in a list
"""
Notes:
- I think you can do better than this. The function you have looks very much like C code. Please view inline
below some issues to fix.
"""

# fixme: it is not correct to name a variable 'list' because the list() class will now not be
#  available within the function; Python does not stop you from overwriting inbuilt function/classes
#  but this harms your code
# fixme: the size of a list can always be assessed using len(); therefore, it is not necessary to
#  pass size as a parameter
def sum_of_list(list, size):
    # todo: include a docstring; see class notes on how to do this
    # size = len(list)
    # return list[size - 1] + sum_of_list(list, size - 1)

    # total_list = sum_of_list(list1, len(list1))
    # print(f"Sum of all elements in a given list= {total_list}")

    # total_list = sum_of_list(list, size)
    # fixme: observe what the output of the following is
    #print(type(list))
    #new_list = list() # now we can't use list anymore!
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

