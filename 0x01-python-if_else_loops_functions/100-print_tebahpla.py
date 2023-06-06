#!/usr/bin/python3
case_switch = True
for i in range(90, 64, -1):
    if case_switch:
        print("{:c}".format(i + 32), end="")
    else:
        print("{:c}".format(i), end="")
    case_switch = not case_switch
print()
