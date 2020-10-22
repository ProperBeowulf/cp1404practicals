"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os




def main():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            complete_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(complete_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    previous_character = ""
    final_name = ""
    for character in new_name:
        if character.isupper() and previous_character.isalpha():
            final_name += "_"
        if not previous_character.isalpha() and previous_character != "'":
            character = character.upper()
        final_name += character
        previous_character = character
    return final_name.replace(".Txt", ".txt")


main()


