from prac_08.taxi import Taxi
from prac_08.silverservicetaxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2)]
    menu_choice = input("Q)uit, C)hoose taxi, D)rive").upper()
    while menu_choice != "Q":
        if menu_choice == "C":
            print("a")
        elif menu_choice == "D":
            print("a")
        menu_choice = input("Q)uit, C)hoose taxi, D)rive").upper()
    print("bye")
