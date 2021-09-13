#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    N = list(my_list)
    if idx < 0:
        return N
    elif idx > len(my_list) - 1:
        return N
    else:
        N[idx] = element
        return N
