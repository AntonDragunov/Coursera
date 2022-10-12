from math import sqrt


def sq_sum(*args):
    s = 0
    for i in args:
        s += i**2
    return print(s)


sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
