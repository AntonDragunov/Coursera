import math

n = int(input())
my_list = []


def pascal(n):
    i = 0
    my_list = []
    while i <= n:
        my_list.append(int(math.factorial(n) / (math.factorial(i) * math.factorial(n - i))))
        i += 1
    return my_list


j = 1
while j <= n:
    for item in (pascal(j - 1)):
        print(item, end=' ')
    print()
    j += 1
