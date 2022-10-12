import random

list_tickets = []
b = []
numbers = list(range(10))
i = 1
while i <= 100:
    b = random.sample(numbers, 7)
    while b[0] != 0 and b not in list_tickets:
        list_tickets.append(b)
        i +=1

for item in list_tickets:


    print(*item, sep='')
