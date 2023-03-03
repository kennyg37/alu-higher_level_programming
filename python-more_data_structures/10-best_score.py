#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    max_num = a_dictionary[0]
    for i in a_dictionary:
        if max_num < i:
            max_num = i
    return max_num
