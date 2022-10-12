list_input = list(map(str, input().split()))
list_new = []

i = 0


list_new.append([])


def chunked(list_input):
    s = 0
    while s < len(list_input):
        list_new.append(list(list_input[s]))
        s += 1



    new_listCh = []

    i = j = 0
    while i < len(list_input):
        #list_new2 = []
        j = 0
        while j < (len(list_input) - i-1):
            #print(i, j)
            m = 0
            list_new2 = []
            while m <= (i+1):
                list_new2.append(list_input[j+m])

                #print(list_new2, 'LIST_new2', i, j, m)

                #print('"список элементов с количеством m=', m)
                m +=1
            new_listCh.append(list_new2)
            #print('новый список', new_listCh)
            j += 1
            #i += 1
        #print('-------------------')
        #new_listCh.append(list_new2)
        #print('"НОВЫЙ СПИСОК')
        #print(new_listCh)
        i += 1
        j += 1

    for item in new_listCh:
        list_new.append(item)
    return print(list_new)




chunked(list_input)

# while i < len(list_input):
#
#     list_new.append(list(list_input[i]))
#     i +=1
# print(list_new)