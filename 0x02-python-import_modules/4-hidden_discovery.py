#!/usr/bin/python3
export PYTHONPATH="D:\alx\alx-higher_level_programming\0x02-python-import_modules\hidden_4.pyc":$PYTHONPATH
if __name__ == "__main__":
    """Print hidden_4 module"""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)