import random


def main():
    quick_picks = []
    number_of_user_picks = int(input("how many quick picks would you like: "))
    for number in range(number_of_user_picks):
        for pick in range(6):
            quick_pick_number = random.randint(1, 45)
            while quick_pick_number in quick_picks:
                quick_pick_number = random.randint(0, 45)
            quick_picks.append(quick_pick_number)
        quick_picks.sort()
        print(quick_picks)
        quick_picks.clear()


main()
