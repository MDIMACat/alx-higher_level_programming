#!/usr/bin/python3
def remove_char_at(str, n):
    for c in range(len(str)):
        if (c == n):
            print("", end="")
        else:
            print(str[c], end="")
    return(" ")