import sys


def main():
    sentence = str(input("Enter a sentence: "))
    sent_join = ''.join(sentence).split()
    print(sent_join)
    sent_index = list(enumerate(sent_join))
    # print(sent_index)
    for x, y in sent_index:
        print(f"{x} -> {y}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
