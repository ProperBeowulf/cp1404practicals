from prac_06.guitar import Guitar


def main():
    gibson_l5_ces = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 500.00)
    print(gibson_l5_ces)
    print(another_guitar)
    print("{} get_age() - Expected 98. Got {}".format(gibson_l5_ces.name, gibson_l5_ces.get_age()))
    print("{} get_age() - Expected 7. Got {}".format(another_guitar.name, another_guitar.get_age()))
    print("{} is_vintage() - Expected True. Got {}". format(gibson_l5_ces.name, gibson_l5_ces.is_vintage()))
    print("{} is_vintage() - Expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))


main()
