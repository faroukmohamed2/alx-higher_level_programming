#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """print reversed"""
    leng = len(my_list) - 1
    for i in range(leng, 0):
        print("{:d}".format(my_list[i]))