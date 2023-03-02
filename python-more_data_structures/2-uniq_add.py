#!/usr/bin/python3
def uniq_add(my_list=[]):
    un_integers = set(my_list)
    num = 0
    for i in un_integers:
        num += i
    return num
