import random

n = str(input())

n = list(n)

random.shuffle(n)

print(*n, sep='')
