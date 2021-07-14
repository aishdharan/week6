import sys

"""
Notes:
- Very good attempt! There are some areas for improvement (see below)
- Very good idea to use recursion!
"""


# fixme: the name 'char_palindrome' does not convey what this function does; can you come up with a better name?
def char_palindrome(char):
    # todo: add a docstring; see class notes on how to do this
    if len(char) < 1:
        # fixme: this is not correct; an empty string is not a palindrome
        return True
    elif char[0] == char[-1]:
        return char_palindrome(char[1:-1])
    else:
        return False


def main():
    string_ = str(input("Enter a string: "))
    if char_palindrome(string_) == True:
        print("This is a palindromic string.")
        print(f"Given string in reverse: {string_[::-1]}")
    else:
        print("This is not a palindromic string.")
        print(f"Given string in reverse: {string_[::-1]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
