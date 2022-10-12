import random

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
random.shuffle(matrix)
print(matrix)
a = []

for item in matrix:
    random.shuffle(item)
    a.append(item)

print(a)