COLOURS = {"black": "#000000", "brown": "#a52a2a", "blue": "#0000ff", "coral": "#ff7f50", "gold": "#ffd700",
           "green": "	#00ff00", "maroon": "#b03060", "orange": "#ffa500", "pink": "#ffc0cb", "purple": "#a020f0"}


user_colour = input("Enter a colour: ").lower()
while user_colour != "":
    if user_colour in COLOURS:
        print(user_colour, "is", COLOURS[user_colour])
    else:
        print("Colour not in dictionary, please choose another")
    user_colour = input("Enter a colour: ").lower()
