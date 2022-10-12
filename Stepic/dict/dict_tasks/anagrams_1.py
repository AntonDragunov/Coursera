dict1, dict2 = {}, {}
for i in input():
    dict1[i] = dict1.setdefault(i, 0) + 1
for i in input():
    dict2[i] = dict2.setdefault(i, 0) + 1
print('YES' if dict1 == dict2 else 'NO')
print(dict1)
print(dict2)