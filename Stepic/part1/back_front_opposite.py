n = list(map(int, input().split()))
#print(len(n))
#print(len(n) // 2)
m = []
i = 1
if len(n) % 2 == 0:
    while i <= (len(n)):
        m.append(n[i])
        #print(m)
        m.append(n[i - 1])
        #print(m)
        i += 2
else:
    while i < (len(n) - 1):
        m.append(n[i])
        #print(m)
        m.append(n[i-1])
        i += 2
        #print(m)
    m.append(n[len(n) - 1])
#print(m)
a = ''
for item in m:
    a = a + str(item)
    a = a + ' '
a.rstrip(' ')
print(a)