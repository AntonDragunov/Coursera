import random

length = int(input())  # длина пароля

password = ''

for i in range(length):
    z = random.random()
    if z < 0.5:
        a = random.randint(65, 90)
        password = password + chr(a)

    else:
        a = random.randint(97, 122)
        password = password + chr(a)
        print(password)


print(password)
