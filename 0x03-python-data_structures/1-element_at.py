#!/usr/bin/python3
def element_at(my_list, idx):
    """print the my_list[idx]"""
    leng = len(my_list) - 1
    if (idx < 0 or idx > leng):
        return (None)
    else:
        return (my_list[idx])