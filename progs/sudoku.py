# Sudoku

# each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
# each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
# each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.

# numbers must be present ONLY once

NUMBER_OF_LINES = 9


def one_to_nine(input_text: str) -> bool:
    """all_there
    Verify that all 1-9 integers are present

    Args:
        input_text (str): [description]

    Raises:
        TypeError: [description]
        ValueError: [description]

    Returns:
        bool: [description]
    """
    expected = [str(i) for i in range(1, 10)]
    if not input_text.isdecimal():
        raise TypeError
    elif len(input_text) != 9:
        raise ValueError
    elif sorted(input_text) == expected:
        return True
    else:
        return False


def all_there(sequences: str) -> bool:

    for sequence in sequences:
        if not one_to_nine(sequence):
            return False
    return True


def get_rows(input_text: str) -> list:
    return [x.strip() for x in input_text.strip().split("\n")]


def get_columns(input_text: str) -> list:

    rows = get_rows(input_text)

    cols = [""] * 9
    for j in range(9):
        for row in rows:
            cols[j] += row[j]

    return cols


def get_squares(input_text: str) -> list:

    squares = [""] * 9
    rows = get_rows(input_text)

    for i in range(3):
        for j in range(3):
            squares[3 * i] += rows[3 * i + j][:3]
            squares[3 * i + 1] += rows[3 * i + j][3:6]
            squares[3 * i + 2] += rows[3 * i + j][6::]

    return squares


def main(input_text: str):

    rows = get_rows(input_text)
    cols = get_columns(input_text)
    squares = get_squares(input_text)
    print(rows)
    print(cols)
    print(squares)

    if all_there(rows + cols + squares):
        print("Yes")
        return True
    else:
        print("No")
        return False


if __name__ == "__main__":

    # Working example
    input_text = """
    295743861
    431865927
    876192543
    387459216
    612387495
    549216738
    763524189
    928671354
    154938672
    """

    # input_text = ""
    # for i in range(NUMBER_OF_LINES):
    #     while True:
    #         new_line = input("%d ==> " % (i + 1))
    #         if new_line.isdecimal():
    #             input_text += new_line + "\n"
    #             break

    assert main(input_text.strip()) == True

    # Failing example
    input_text = """
    195743862
    431865927
    876192543
    387459216
    612387495
    549216738
    763524189
    928671354
    254938671
    """

    assert main(input_text.strip()) == False
