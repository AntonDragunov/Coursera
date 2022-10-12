n = int(input())
k = int(input())
d = []
i = 1
while i <= n:
    d.append(i)
    i += 1
#print(d)

i = 0


def circle(d, i):
    while i < k - 1:
        d.append(d[0])
        #print(d, 'Добавляем первый символ в конец')
        d.pop(0)
        #print(d, 'удаляем первый симовл')
        i += 1
    d.pop(0)
    return d

e=''
while len(d) != 1:

    circle(d, i)
    #print(d, 'удалили символ совсем из списка!')
e = d[0]
print(int(e))

