def digit_of_life(number: str) -> str:

    if number.isdecimal():
        num_sum = 0
        for char in number:
            num_sum += int(char)
        sum = str(num_sum)
        if len(sum) > 1:
            return digit_of_life(sum)
        elif len(sum) == 1:
            return sum
        else:
            raise ValueError
    else:
        raise ValueError


def main():

    try:
        date = input("Enter Birthday as YYYYMMDD or MMDDYYYY or YYYYDDMM -> ")
        print(digit_of_life(date))
    except ValueError:
        print("%r is an invalid input" % date)


if __name__ == "__main__":
    main()
