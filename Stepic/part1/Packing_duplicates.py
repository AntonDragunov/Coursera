n = list(map(str, input().split()))
# print(n)
#print(len(n))
m = n.copy()
new_list = []
new_list_2 = []
i = 0
j = 1

while i <= (len(n)-1):

    #print(i, j, 'начинаем новый список')
    new_list_2 = []
    new_list_2.append(n[j-1])
    #rint(new_list_2)
    #print(n[j])
    while n[j] == n[j-1]:
        new_list_2.append(n[j])
        #print(new_list_2)
        j += 1
        if j == (len(n)):
            break
        else:
            pass
    #print(j, i, 'записываем список')
    new_list.append(new_list_2)
    #print(new_list)
    j += 1
    i = j
    if j == (len(n)):
        new_list_2 = []
        new_list_2.append(n[j-1])
        new_list.append(new_list_2)
        i = len(n)
    else:
        pass


print(new_list)
# a a a b g a t a
