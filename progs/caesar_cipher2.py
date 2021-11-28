# Caesar cipher.

# allow shifting characters by a different value 1-25
# maintain case after shifting


import argparse

DEFAULT_SHIFT = 1
MIN_SHIFT = 1
MAX_SHIFT = 25
MOVE_UP_ONE_LINE = "\033[F"
DISPLAY = "=> %s"


def get_shift(min: int = MIN_SHIFT, max: int = MAX_SHIFT) -> int:
    """get_shift

    Args:
        min (int, optional): Minimum shift value (inclusive). Defaults to MIN_SHIFT.
        max (int, optional): Maximum shift value (inclusive). Defaults to MAX_SHIFT.

    Returns:
        int: shift value
    """
    prompt = "Please Enter a shift value [1-25]: "
    while True:
        num = input(prompt)
        if num.isdecimal():
            num = int(num)
            if num >= min and num <= max:
                return num
        print("%sTry again... " % MOVE_UP_ONE_LINE)


def encrypt(text: str, shift: int = DEFAULT_SHIFT) -> str:
    """encrypt
        Caesar cipher, with shift value [1-25].
        Preserves case
        non-alphanumeric characters are preserved
    Args:
        text (str): original text
        shift (int, optional): cipher shift [1-25]. Defaults to 1.

    Returns:
        str: cipher
    """
    cipher = ""
    for char in text:
        if not char.isalpha():
            cipher += char
        else:
            if char.isupper():
                offset = ord("A")
            else:
                offset = ord("a")
            code = offset + (ord(char) + shift - offset) % 26
            cipher += chr(code)
    return cipher


def decrypt(cipher: str, shift: int = DEFAULT_SHIFT) -> str:
    return encrypt(cipher, -shift)


def main(text, shift, decode: bool = False):
    """Main

    Args:
        text ([type]): input text
        shift ([type]): shift value for cipher [1-25]
        decode (bool, optional): Decode when set, Encode otherwise. Defaults to False.
    """

    if decode:
        result = decrypt(text, shift)
    else:
        result = encrypt(text, shift)

    print(DISPLAY % result)


if __name__ == "__main__":

    # Get CLI Paramaters
    parser = argparse.ArgumentParser(description="Caesar cipher")
    parser.add_argument("--decrypt", "-d", action="store_true")

    args = parser.parse_args()

    text = input("Enter your message: ")
    shift = get_shift()

    main(text, shift, decode=args.decrypt)
