#!/usr/bin/python3
if __name__ == "__main__":
    """Prints all the names defined by the compiled module hidden_4.pyc"""
    import hidden_4

    n = dir(hidden_4)
    for i in range(n):
        if n[:2] != "__":
            print(n)
