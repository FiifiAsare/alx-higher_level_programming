#!/bin/python3
of __name__ == "__main__":
    """Print all names defined by hidden 4 module."""
    import hidden_4
    names = dir(hidden_4)
    for name in names:
        if name[:] != "__":
            print(name)
