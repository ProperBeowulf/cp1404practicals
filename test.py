def main():
    squared_number = square_function()
    print(squared_number)


def square_function():
    number = int(input("please enter a number: "))
    total = number * number
    return total


main()
