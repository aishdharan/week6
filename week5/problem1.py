import random
import sys


def main():
    # l1 = [1, 2, 3]
    l1 = random.choices(range(0, 101), k=100)
    # l2 = [4, 5, 6]
    l2 = random.choices(range(0, 101), k=100)
    print(f"l1 = {l1}")
    print(f"l2 = {l2}")
    list_zip = list(zip(l1, l2))
    # print(list_zip)
    l3_sum = []
    l3_product = []
    for x, y in list_zip:
        l3_sum.append(x + y)
        l3_product.append(x * y)
    print(f"l3_sum = {l3_sum}")
    print(f"l3_product = {l3_product}")
    print(f"cumulative product= {sum(l3_product)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
