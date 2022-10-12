n = str(input())
m = str(input())
reference = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

if set(n + m) == reference:
    print('YES')
else:
    print('NO')
