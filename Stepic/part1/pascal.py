import math
n = int(input())
my_list = []


def pascal(n):
    i = 0
    while i <= n:
        my_list.append(int(math.factorial(n) / (math.factorial(i) * math.factorial(n - i))))
        i += 1
    return my_list


print(pascal(1))
