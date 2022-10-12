import random

n = int(input())  # количество попыток


for i in range(n):
    a = random.random()
    if a < 0.5:
        print('Орел')
    else:
        print('Решка')
