import random

a = []






for i in range(7):
    b = random.randint(1,49)
    while b in a:
        b = random.randint(1,49)
    a.append(b)

a.sort()
print(*a)