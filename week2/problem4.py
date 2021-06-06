import os
import sys
import math


def calculate(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        # here is where complex roots appear
        return None, None
    # if discriminant >= 0 then we get real roots
    x1 = complex((2 * c) / (- b + math.sqrt(discriminant)))
    x2 = complex((2 * c) / (- b - math.sqrt(discriminant)))
    return x1, x2


def main():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    x1, x2 = calculate(a, b, c)
    print(f"x1={x1}, x2={x2}")
    # return value of exit status
    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())