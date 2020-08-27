def main():

    numbers = [3, 1, 4, 1, 5, 9, 2]
    numbers.remove(3)
    numbers.insert(0, 10)
    numbers.remove(2)
    numbers.insert(6, 1)
    print(numbers)
    numbers2 = slice(2, 6)
    print(numbers[numbers2])
    if 9 in numbers:
        print("yes")
    else:
        print("no")

# question 1: will print 3
# question 2: starts at the end of the list and works to the front
# question 3: will print 1
# question 4: starts at beginning goes till end
# question 5: will print 1 and 5
# question 6: will look through list for the when the number 5 appears
# question 7: will look for 7 in list
# question 8: will look through list for 3, won't find since expecting int
# question 9 : will add need to have equals new list as trying to combine 2 lists would need to .append if wanted to
# add them to the original list

main()
