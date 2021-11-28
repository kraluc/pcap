# Palindrome test

# assume that an empty string isn't a palindrome;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check - treat them as non-existent; (done)
# there are more than a few correct solutions - try to find more than one.

input_text = input("Enter a word: ")
clean = "".join([x for x in input_text if x.isalpha()]).casefold()

if clean[::-1] == clean and len(input_text):
    print("It's a palindrome")
else:
    print("It's not a palindrome")
