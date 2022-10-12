n = int(input())
slang = []
for i in range(n):
    slang.append(str(input()))

result = {c[:(c.index(': '))].lower(): c[((c.index(': ')) + 2):] for c in slang}
print(result)
m = int(input())

for i in range(m):
    a = input().lower()
    if a in result:
        print(result[a])
    else:
        print('Не найдено')
