#!/usr/bin/python3
if __name__ == "__main__":
    """infinty addition"""
    import sys
    siz = len(sys.argv) - 1
    result = 0
    for i in range(siz):
        result = result + int(sys.argv[i + 1])
    print(result)
