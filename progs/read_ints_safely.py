# Read_ints_safely.py

# our task is to write a function able to input integer values and to check
# if they are within a specified range.

# The function should:

#     accept three arguments: a prompt, a low acceptable limit, and a high acceptable limit;
#     if the user enters a string that is not an integer value,
#         the function should emit the message Error: wrong input, and ask the user to input the value again;
#     if the user enters a number which falls outside the specified range,
#         the function should emit the message Error:
#         the value is not within permitted range (min..max) and ask the user to input the value again;
#     if the input value is valid, return it as a result.


def read_int(prompt: str, min: int, max: int) -> int:

    try:
        number = int(input(prompt))
        assert min <= number <= max
        return number
    except ValueError:
        print("Error: wrong input")
        return read_int(prompt, min, max)
    except AssertionError:
        print(
            "Error: the value is not within the permitted range (%d..%d)" % (min, max)
        )
        return read_int(prompt, min, max)


v = read_int("Enter a number from -10 to 10: ", -10, 10)
print("The number is: ", v)
