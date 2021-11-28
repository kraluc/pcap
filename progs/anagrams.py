# ANAGRAMS.py

# An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once.
# For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.
# Your task is to write a program which:

#     asks the user for two separate texts;
#     checks whether, the entered texts are anagrams and prints the result.

# Note:

#     assume that two empty strings are not anagrams;
#     treat upper- and lower-case letters as equal;
#     spaces are not taken into account during the check - treat them as non-existent

# Test your code using the data we've provided.

print("Anagrams:")


def get_word(msg: str = "") -> str:
    while True:
        word = input(msg + " word -> ")
        if word.isalpha() and len(word):
            return word
        else:
            print("invalid... try again")


def sorted_letters(word: str) -> str:
    # sort the characters, map all to lowercase and ignore whitespaces
    return "".join(sorted(word.casefold())).strip()


def main():
    word1 = get_word("1st")
    word2 = get_word("2nd")

    if (sorted_letters(word1) == sorted_letters(word2)) and len(word1) and len(word2):
        print("=> Anagrams")
    else:
        print("=> Not anagrams")


if __name__ == "__main__":
    main()
