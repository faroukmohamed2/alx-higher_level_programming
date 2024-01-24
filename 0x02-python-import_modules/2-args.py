#!/usr/bin/python3
if __name__ == "__main__":
    """
    print arguments
    """
    import sys
    count = len(sys.argv) - 1
    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument".format(count))
    else:
        print("{} arguments:".format(count))
    for i in range(0, count):
        print("{}: {}".format(i, sys.argv[i + 1]))