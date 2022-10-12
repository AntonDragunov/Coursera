n = int(input())  # общее число учеников
list_pupils = []
for i in range(n):
    list_pupils.append(input())

secret_pairs = []
pair = []
j = 0 # дополнительный счетчик


for item in list_pupils:


    for i in range(n):
        #print(j, i)
        if i == j:
            #print('РАВЕНСТВО!')
            pass

        else:
            pair = []
            pair.append(item)
            pair.append('-')
            pair.append(list_pupils[i])
            pair = tuple(pair)
            secret_pairs.append(pair)
            #print(j , i , secret_pairs[-3:])

    j += 1

#print(list_pupils)
for item in secret_pairs:
    print(*item, end='\n')