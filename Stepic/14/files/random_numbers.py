import random

numbers = []
numbers = [i for i in range(111, 778)]

s = random.sample(numbers, 25)

with open('random.txt', 'w', encoding='utf-8') as file:
    # file.writelines(str(s))
    print(*s, sep='\n', file=file)
