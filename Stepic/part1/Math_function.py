import math


def kvadrat():
    return n**2


def cube():
    return n**3

def sgrt():
    return math.sgrt(n)

def module():
    return abs(n)

def sinus():
    return math.sin(n)


functions = {'квадрат': kvadrat, 'куб': cube, 'корень': sgrt, 'модуль': module, 'синус': sinus}
n = int(input())
function = input()

print(functions[function]())
