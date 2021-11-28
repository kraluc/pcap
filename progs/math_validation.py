import math


def valid_float(text: str) -> float:
    # remove spaces
    text = text.strip()

    # Check whether text is a positive number
    if text == "":
        raise ValueError
    elif text[0] in ["+", "-"]:
        if len(text) < 2:
            raise ValueError
        elif text[1::].isdecimal():
            return float(text)
        elif text[1::].find(".") == text[1::].rfind("."):
            return float(text)
        else:
            raise ValueError
    elif text.isdecimal():  # No leading sign and no separator
        return float(text)
    elif text.find(".") == text.rfind("."):  # No leading sign with separator
        if len(text) < 2:
            raise ValueError
        elif text.replace(".", "").isdecimal():  # No leading + with ONE '.' separator"
            return float(text)
        else:
            raise ValueError
    else:
        raise ValueError


def valid_int(text: str) -> int:

    if text == "":
        raise IndexError
    elif text[0] in ["+", "-"]:
        if text[1::].isdecimal():
            return int(text)
        else:
            raise ValueError
    elif text.isdecimal():
        return int(text)
    else:
        raise ValueError


def main():
    # get a valid positive float - accepts leading '+' and possible presence of a single '.' and at least one digit
    while True:
        try:
            x = valid_float(input("Enter a positive float: "))
            if x > 0:
                break
            raise ValueError
        except ValueError:
            print("Try again")

    y = math.sqrt(x)

    print("The square root of", x, "equals to", y)

    # get a valid pair of integers - the 2nd number must be different from 0

    while True:
        try:
            x = valid_int(input("Enter a +/- integer different from 0: "))
            y = 1 / x
            print("%d/%d = %.5f" % (int(x / abs(x)), abs(x), y))
            break
        except ValueError:
            print("Must be an integer...")
        except ZeroDivisionError:
            print("Must be non-zero...")
        except IndexError:
            print("Must be an integer...")


if __name__ == "__main__":
    main()
