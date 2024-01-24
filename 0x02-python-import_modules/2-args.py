#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1

    if count == 1:
        print("1 argument:")
    elif count > 1:
        print("{} arguments:".format(count))
    else:
        print("0 arguments.")
    for i in range(1, count + 1):  
        print("{}: {}".format(i, sys.argv[i]))
    print()