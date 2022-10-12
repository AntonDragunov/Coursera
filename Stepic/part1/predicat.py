def func(num1, num2):
    return num1 % num2 == 0

num1, num2 = int(input()), int(input())

if func(num1, num2):
    print('делится')
else:
    print('не делится')


