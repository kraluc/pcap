# Caesar cipher.

import argparse


def encrypt(text: str) -> str:
    cipher = ""
    for char in text:
        if not char.isalpha():
            continue
        char = char.upper()
        # shift alphabet characters by one letter
        code = ord(char) + 1
        if code > ord("Z"):
            code = ord("A")
        cipher += chr(code)
    return cipher


def decrypt(cipher: str) -> str:
    text = ""
    for char in cipher:
        if not char.isalpha():
            continue
        code = ord(char) - 1
        if code < ord("A"):
            code = ord("Z")
        text += chr(code)
    return text


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Caesar cipher")
    parser.add_argument("--decrypt", "-d", action="store_true")

    args = parser.parse_args()

    text = input("Enter your message: ")
    print(text)

    if args.decrypt:
        print("cipher: %r" % text)
        print("original:   %r" % decrypt(text))
    else:
        print("original:  %r" % text)
        print("cipher:    %r" % encrypt(text))
