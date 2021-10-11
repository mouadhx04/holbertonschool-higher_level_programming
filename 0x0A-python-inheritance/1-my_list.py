#!/usr/bin/python3
""" Mylist Module """


class MyList(list):
    """
    MyList class that inherits from list
    """
    def print_sorted(self):
        """
        prints sorted list of ints sorted (ascending sort).
        """
        print(sorted(self))
