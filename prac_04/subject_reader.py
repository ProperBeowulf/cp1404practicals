"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_data(data)


def get_longest_name(data):
    """find the longest name in list"""
    longest_name = 0
    for data_point in data:
        if len(data_point[1]) > longest_name:
            longest_name = len(data_point[1])
    return longest_name


def display_data(data):
    longest_name = get_longest_name(data)
    for data_point in data:
        print("{} is taught by {:<{}} and has {:<3} students". format(data_point[0], data_point[1], longest_name,
                                                                   data_point[2]))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    finished_list = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        finished_list.append(parts)

    input_file.close()
    return finished_list


main()
