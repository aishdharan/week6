import random
import sys


def main():
    # l1 = [1, 2, 3, 4]
    l1 = random.choices(range(0, 101), k=100)
    # l2 = [5, 6, 7, 8]
    l2 = random.choices(range(0, 101), k=100)
    print(f"l1 = {l1}")
    print(f"l2 = {l2}")
    list_zip = list(zip(l1, l2))
    # print(list_zip)
    l3_sum = []
    l3_product = []
    l3_even = []
    l3_odd = []

    for x, y in list_zip:
        l3_sum.append(x + y)
        l3_product.append(x * y)
        if x % 2 == 0 and y % 2 == 0:
            l3_even.append(x + y)
        elif x % 2 != 0 and y % 2 != 0:
            l3_odd.append(x + y)
    print(f"l3_sum = {l3_sum}")
    print(f"l3_product = {l3_product}")
    print(f"cumulative product= {sum(l3_product)}")
    print(f"l3_even = {l3_even}")
    print(f"l3_odd = {l3_odd}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
