coefficients = list(map(int, input().split()))
x = int(input())
#print(len(coefficients))
from functools import reduce


def evaluate(coefficients, x):
    i = 0
    new_list = map(lambda w, i: w * x**i, list(reversed(coefficients)), (range(0, len(coefficients))))
    #print(*new_list)
    summa = reduce(lambda z, y: z + y, list(new_list), 0)

    return print(summa)



evaluate(coefficients, x)




