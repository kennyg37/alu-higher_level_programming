#!/usr/bin/python3
def no_c(my_string):
    # Convert the string to a list of characters
    char_list = list(my_string)

    # Loop over each character in the list and remove 'c' and 'C'
    for char in ['c', 'C']:
        while char in char_list:
            char_list.remove(char)

    # Convert the list of characters back to a string
    new_string = "".join(char_list)

    # Return the modified string
    return new_string
