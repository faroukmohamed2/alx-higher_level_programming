#!/usr/bin/python3
if __name__ == "__main__":
    """
    print arguments
    """
    import sys
    count = len(sys.argv)
    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument".format(count))
    else:
        print("{} arguments:".format(len(argv)))
    for i in range(1, len(argv) + 1):
        print("{}: {}".format(count, sys.argv[i]))