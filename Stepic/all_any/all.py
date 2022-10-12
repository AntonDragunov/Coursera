numbers = [10, 30, 20, 50, 40, 60, 70, 80]

total = 0
for index, number in enumerate(numbers, 1):
    if index % 2 == 0:
        total += number
print(total)
