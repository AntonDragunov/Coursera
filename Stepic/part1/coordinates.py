n = int(input())  # вводим количество точек
k = []
i = 0
while i < n:
    k.append(input().split())
    i += 1


#print(k[0])
#print(k[1])
q1 = q2 = q3 = q4 = 0
f = []
for j in k:
    #f.append(j)
    #print(f)
    #print(len(f))
    if int(j[0]) == 0 or int(j[1]) == 0:
        pass
    else:
        if int(j[0]) > 0 and int(j[1]) > 0:
            q1 += 1
        elif int(j[0]) > 0 and int(j[1]) < 0:
            q4 += 1
        elif int(j[0]) < 0 and int(j[1]) < 0:
            q3 += 1
        else:
            q2 += 1

print('Первая четверть:',q1)
print('Вторая четверть:',q2)
print('Третья четверть:',q3)
print('Четвертая четверть:',q4)
