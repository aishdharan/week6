import sys


def char_palindrome(char):
    if len(char) < 1:
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
