#!/usr/bin/python3
def no_c(my_string):
    L = ""
    for i in my_string:
        if not (i == 'c' or i == 'C'):
            L += i
    return L
