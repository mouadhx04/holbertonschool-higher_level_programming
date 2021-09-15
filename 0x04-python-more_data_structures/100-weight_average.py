#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        tot = 0
        freq = 0
        for tup in my_list:
            (w, o) = tup
            tot += (w * o)
            freq += o
        return (tot /freq)
