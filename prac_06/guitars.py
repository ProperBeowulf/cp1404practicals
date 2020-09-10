from prac_06.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print("{} ({}) : {} added.".format(name, year, cost))
        name = input("Name: ")

    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage_string = " (vintage) " if guitar.is_vintage() else " "
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                  vintage_string))


main()
