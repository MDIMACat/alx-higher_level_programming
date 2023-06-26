def safe_print_division(a, b):
    c = 0
    try:
        c = a / b
    except (ZeroDivisionError, ValueError):
        c = None
    finally:
        print("Inside result: {:d}".format(c))
        return c
