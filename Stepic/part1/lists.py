list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0
for li in list1:
    for m in li:
        total += int(m)
        counter += 1

print(total / counter)
