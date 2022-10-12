n = int(input())
tribbonachi = [1, 1, 1]
i = 3
if n > 3:
    while i < n:
        s = tribbonachi[i - 1] + tribbonachi[i - 2] + tribbonachi[i - 3]
        tribbonachi.append(s)
        i += 1
    print(*tribbonachi)
elif n > 2:
    print('1 1 1')
elif n > 1:
    print('1 1')
else:
    print('1')
