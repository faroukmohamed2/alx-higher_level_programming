#!/usr/bin/python3
if __name__ == "__main__":
    """hidden"""
    import hidden_4.pyc
    names = dir(hidden_4.pyc)
    for name in names:
        if name[:2} != "__":
            print(name)