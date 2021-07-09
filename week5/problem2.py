import random
import sys


def main():
    l = random.choices(range(0, 101), k=100)
    print(f"l = {l}")
    print(len(l))
    new_l = list()
    i = 0
    j = 0
    # cumulative sum
    while i < len(l):
        j += l[i]
        i += 1
        new_l.append(j)
    print(f"new_l = {new_l}")
    print(len(new_l))

    new_l1 = list()
    k = 0
    # adjoin pair sum
    while k < (len(l) - 1):
        new_l1.append(l[k] + l[k + 1])
        k += 1
    print(f"new_l1 = {new_l1}")
    print(len(new_l1))

    new_l2 = list()
    u = 0
    # sum of three alternate values
    while u < (len(l) - 4):
        new_l2.append(l[u] + l[u + 2] + l[u + 4])
        u += 1
    print(f"new_l2 = {new_l2}")
    print(len(new_l2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
