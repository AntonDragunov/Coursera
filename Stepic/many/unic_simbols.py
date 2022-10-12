n = int(input())
b = []
a = ''
for i in range(n):
    a = str(input()).upper()
    b.append(a)

for item in b:
    print(len(set(item)))
