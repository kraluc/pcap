# find a word

# using the find() method for searching strings.

# Your task is to write a program which answers the following question: are the characters
# comprising the first string hidden inside the second string?

# For example:

#     if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
#     if the second string is "vcxzxdcybfdstbywuefsas", the answer is no
#        (as there are neither the letters "d", "o", or "g", in this order)

#    you should use the two-argument variants of the pos() functions inside your code;
#    don't worry about case sensitivity.
#    order of letters matters


def word(msg: str = "") -> str:
    return input(msg + " word -> ")


def spell(word: str) -> list:
    return [c for c in word]


def main():

    word1 = word("1st").casefold()
    word2 = word("2nd").casefold()

    if len(word2) < len(word1):
        print("No")
    else:
        while len(word1):
            found = word2.find(word1[0])
            if found < 0:
                print("No")
                break
            word2 = word2[found + 1 : :]
            word1 = word1[1::]
        if found >= 0:
            print("Yes")


if __name__ == "__main__":
    main()
