#!/usr/bin/env python


def mysplit(strng):

    result = []
    word = ""
    # remove all leading spaces
    # if character is not a space, add it to word
    # if character is a space, check whether that word is not empty
    # and, if so, move the word to the result list

    while len(strng) > 0:
        character = strng[0]
        if character.isalpha():
            word += character
        else:
            if len(word) > 0:
                result.append(word)
            word = ""
        strng = strng[1::]
    else:
        return result


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
