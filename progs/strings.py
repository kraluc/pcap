# Example 1
from typing import Type


word = "by"
print(word)
print(len(word))

# Example 2
empty = ""
print(empty)
print(len(empty))

# Example 3
i_am = "I'm"
print(i_am)
print(len(i_am))

# Example 4: Multiline
multiline = """Line #1
Line #2"""
print(multiline)
print(len(multiline))

# Example 5: Concatention (+) and Replication (*)
str1 = "a"
str2 = "b"

print(str1 + str2)
print(str2 + str1)

print(5 * "a")
print("b" * 4)

# Example 6: Demonstrating the ord() and chr() functions
char_1 = "a"
char_2 = " "  # space

print("%r number is %i" % (char_1, ord(char_1)))
print("%r number is %i" % (char_2, ord(char_2)))

code_point1 = ord(chr(10))
char_x = chr(ord("x"))
print("ord(chr(10)) is %r, of type %r" % (code_point1, type(code_point1)))
print("chr(ord('x')) is %r, of type %r" % (char_x, type(char_x)))
print(code_point1 == 10)
print(char_x == "x")

# code_point = input("Please enter a code point (integer): ")
# try:
#     character = chr(int(code_point))
#     print("code point %r --> character %r" % (code_point, character))
# except ValueError:
#     print("ValueError: %r, invalid code point" % code_point)
# except TypeError:
#     print("TypeError: %r, wrong type " % code_point)


# Example 7: Strings are sequences / indexing
# Indexing strings.

the_string = "silly walks"

for ix in range(len(the_string)):
    print(the_string[ix], end=" ")

print()

# Iterating through a string.

the_string = "silly walks"

for character in the_string:
    print(character, end=" ")

print()

# Example 8: Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

# Example 9: min()
# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))

# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print("[" + min(t) + "]")

t = [0, 1, 2]
print(min(t))

# Example 10: max()
# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))


# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print("[" + max(t) + "]")

t = [0, 1, 2]
print(max(t))

# Example 11: Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))
