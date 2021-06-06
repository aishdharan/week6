import os
import sys
import math


def calculate(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    # real roots here
    x1 = complex((2 * c) / (- b + math.sqrt(discriminant)))
    x2 = complex((2 * c) / (- b - math.sqrt(discriminant)))
    return x1, x2


def main():
    # we haven't covered map(); perhaps you googled?
    # easier to stick to simpler ideas
    # split(", ") - no splitting occurs if user doesn't enter spaces; ValueError
    a, b, c = map(float, input("Please enter the coefficients: ").split(", "))
    x1, x2 = calculate(a, b, c)
    print(f"x1={x1}, x2={x2}")
    # return value of exit status
    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())