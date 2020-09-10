def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    numbers = []
    for i in range(5):
        user_number = int(input("please enter a number: "))
        numbers.append(user_number)
    print(numbers)
    print("first number is {}".format(numbers[0]))
    print("last number is {}".format(numbers[4]))
    print("smallest number is {}".format(min(numbers)))
    print("largest number is {}".format(max(numbers)))
    average_number = sum(numbers) / len(numbers)
    print("average number is {}".format(average_number))

    user_input_name = input("please enter a user name: ")
    if user_input_name in usernames:
        print("Access Granted")
    else:
        print("Access Denied")


main()
