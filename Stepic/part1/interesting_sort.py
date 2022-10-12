numbers = list(map(str, input().split()))
#print(numbers)
numbers.sort()
#print(numbers)
s = 0
i = 0


def summa(number):
    s = 0
    i = 0
    for i in range(len(str(number))):
        number = str(number)
        # print(str(number[i]))
        s += int(number[i])
    return (s, int(number))


data = sorted(numbers, key=summa)

for item in data:
    print(item + ' ', end='')


# 12 14 79 7 4 123 45 90 111
