n = str(input()).split()

if set(n[1]) == set(n[0]) == set(n[2]):
    print('YES')
else:
    print('NO')


