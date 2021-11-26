symbol = "#"
rows = ["  " + symbol, symbol + "  ", symbol + " " + symbol, symbol * 3]

digit_map = {
    "0": "32223",
    "1": "00000",
    "2": "30313",
    "3": "30303",
    "4": "22300",
    "5": "31303",
    "6": "31323",
    "7": "30000",
    "8": "32323",
    "9": "32303",
}


def digit_row(digit: int, row: int) -> str:
    """draw_row

    Args:
        digit (int): number
        row (int): line number to be drawn

    Returns:
        str: digit row symbol
    """
    digit_rows = digit_map.get(digit)
    row_index = int(digit_rows[row])
    return rows[row_index]


number = input("Please, enter an integer: ")
spacer = " "
# iterate over each display row
for row_number in range(5):
    line = ""
    for digit in number:
        line += digit_row(digit, row_number) + spacer
    print(line.rstrip())
