def main():

        total = 0
        items = int(input("please enter Number of Items:"))
        for i in range(items):
            price = float(input("please enter product price:$"))
            total = total + price

        if total > 100:
            discount = total * .10
            print("$", total - discount)
        else:
            print("$", total)


main()
