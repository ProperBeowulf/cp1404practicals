"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = check_score(score)
    print(result)
    random_score = random.randint(0, 100)
    print(random_score)
    random_result = check_score(random_score)
    print(random_result)


def check_score(score):
    if score < 0:
        return ("Invalid score")
    else:
        if score > 100:
            return ("Invalid score")
        elif score >= 90:
            return ("Excellent")
        elif score >= 50:
            return ("Passable")
        elif 0 <= score < 50:
            return ("Bad")


main()
