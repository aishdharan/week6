import sys


def max_min(list1):
    max1 = list1[0]
    min2 = list1[0]
    for num in list1:
        if num > max1:
            max1 = num
        elif num < min2:
            m2 = num
    return max1, min2

    # return m1, m2


def main():
    lst = [1, 5, 8, 9, 45, 67, 86]
    print(max_min(lst))
    return 0


if __name__ == "__main__":
    sys.exit(main())
