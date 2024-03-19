#!/usr/bin/pythonn3
def no_c(my_string):
    """retrun a copy without c or C"""
    new_string = [x for x in my_string if x != 'c' or x != 'C']
    return ("".join(new_string))