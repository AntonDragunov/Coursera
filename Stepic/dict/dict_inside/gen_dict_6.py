numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]

result = {numbers[c]: [j for j in range(1, numbers[c]+1, 1) if numbers[c] % j == 0] for c in range(len(numbers))}

print(result)
