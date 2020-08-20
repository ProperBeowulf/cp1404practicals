output = open("name", "w")
name = input("please enter your name")
print(name, file=output)

output = open("name", "r")
print("Your name is:", output.read())


output2 = open("numbers", "r")
number1 = int(output2.readline())
number2 = int(output2.readline())

print(number1 + number2)
