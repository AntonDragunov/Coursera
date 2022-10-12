import random

n = 10 ** 6  # количество испытаний
s0 = 4
k = 0
for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if (x ** 2 + y ** 2 - 1) <= 0:  # если попадает в нужную область
        k += 1



print((k / n) * s0)