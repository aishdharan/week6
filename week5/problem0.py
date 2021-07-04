import random
import sys

"""
Notes:
- Great job for part (a)
- In part (b) and (c) you have used a relatively complex construct, which to me
either implies that you know far more than I thought or you got some help
from Google. Could you please rewrite them using a simple for loop?
My goal is to know that you know and using a list comprehension while you
struggle with earlier material makes it hard to for me to gauge your
true learning. I hope that makes sense.
"""


def main():
    l = random.choices(range(0, 101), k=100)
    print(f"l = {l}")
    # print(len(l))
    new_l = list()
    # print(new_l)
    j = 0
    # cumulative sum
    for i in l:
        j += i
        new_l.append(j)
    print(f"new_l = {new_l}")
    # print(len(new_l))

    # adjoin pair sum
    # todo: simplify
    #  I'm not interested in the final result; I want to see that you understand
    #  what you are doing. This list comprehension suggest to me that you have an
    #  alternate source (usually Google), which might make you get by in the
    #  short run but which will ultimately mislead you.
    new_l1 = [(l[k] + l[k + 1]) for k in range(0, len(l) - 1)]
    print(f"new_l1 = {new_l1}")

    # sum of three alternate values
    # todo: simplify
    new_l2 = [(l[m] + l[m + 2] + l[m + 4]) for m in range(0, len(l) - 4)]
    print(f"new_l2 = {new_l2}")

    # print(l1[1::1])

    # j1 = 0
    # l1_dict = dict(iter())
    # print(l1_dict)
    # j1 = 0
    # for k, v in l1_dict.items():
    #    j1 = j1 + k + v
    #    new_l1.append(j1)
    # print(j1)
    # for v in l1:
    # print(v)
    # j2 = j1 + v
    # print(j2)
    # print(k)
    # print(v)
    # j = j + k + v
    # new_l2.append(j2)
    # print(new_l1)
    # print(k[0])

    # l1.index()
    # new_l = l1
    # new_l[0] = l1.index(0)
    # new_l[1] = l1.index
    # for _
    # for new_l in l1:
    #    new_l = l1 + 1
    #    print(new_l)

    # print(l1)

    return 0


if __name__ == "__main__":
    sys.exit(main())
