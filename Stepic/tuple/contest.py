n = int(input())
b = []
a = ''
for i in range(n):
    a = str(input())
    b.append(a.split())
for item in b:
    print(*item)
print()
for _ in b:
    if int(_[1]) >= 4:
        print(*_)
    else:
        pass

