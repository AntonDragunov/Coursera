n = int(input())
b = []
a = ''
for i in range(n):
    a = str(input()).upper()
    b.append(a)


konkaten = ''
for item in b:
    konkaten += item


konkaten = set(konkaten)
print(len(konkaten))