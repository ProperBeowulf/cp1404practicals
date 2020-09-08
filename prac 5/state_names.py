"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)
longest_word = 0
longest_key = 0

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

for x in CODE_TO_NAME.values():
    if len(x) > longest_word:
        longest_word = len(x)

for x in CODE_TO_NAME:
    if len(x) > longest_key:
        longest_key = len(x)

count2 = -1
for x in CODE_TO_NAME:
    count2 = count2 + 1
    states_short = list(CODE_TO_NAME.keys())[count2]
    states_long = list(CODE_TO_NAME.values())[count2]
    print("{:<{}} is {:<{}}".format(states_short, longest_key, states_long, longest_word))


