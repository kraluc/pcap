import math


def valid_float(text: str) -> float:
    # remove spaces
    text = text.strip()

    # Check whether text is a positive number
    if text == "":
        raise ValueError
    elif text.find("+") == 0 and text.rfind("+") == 0:  # leading +
        if len(text) < 2:
            raise ValueError
        elif text[1::].isdecimal():
            return float(text)
        elif text[1::].find(".") == text[1::].rfind("."):
            return float(text)
        else:
            raise ValueError
    elif text.isdecimal():
        return float(text)
    elif text.find(".") == text.rfind("."):
        if len(text) < 2:
            raise ValueError
        elif text.replace(".", "").isdecimal():  # No leading + with ONE '.' separator"
            return float(text)
        else:
            raise ValueError
    else:
        raise ValueError


# get a valid positive float - accepts leading '+' and possible presence of a single '.' and at least one digit
while True:
    try:
        x = valid_float(input("Enter a positive float: "))
        break
    except ValueError:
        print("Try again")

y = math.sqrt(x)

print("The square root of", x, "equals to", y)
