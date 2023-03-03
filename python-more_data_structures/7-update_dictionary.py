#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if not key:
        return None
    else:
        a_dictionary[key] = value
    return a_dictionary
