#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    siz = len(sys.argv) - 1
    if siz == 0:
        print("0 arguments.")
    elif siz == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(siz))
    for i in range(siz):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
