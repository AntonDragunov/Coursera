with open('WhatsApp Chat V.txt', 'r', encoding='utf-8') as file:
    list1 = file.read().splitlines()

#print(list1)
b = []
#print(list1)
a = ''
# for item in list1:
#     a += item


#print(a)
c = ''
words = []
znaki = ['>', '<', '\'', '.', ',', ';', '-', '?', '!', '\'\', \'n', ')', '(', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '/']
for item in list1:
    c = ''
    for _ in item:
        if _ not in znaki:
            c += _
        else:
            pass
    words.append(c)
#z = sorted(words)
#print(words)
words2 = []
for item in words:

    words2.append(item.lstrip(':  ').rstrip())
#print(words2)


Valya = []
Anton = []
a = 0
for item in words2:


    if 'Валентина Соколова:' in item:
        #stroka = ''
        Valya.append(item[20:])
        #stroka += item[20:]
        a = 0
    elif 'Антон:' in item:
        #stroka = ''
        Anton.append(item)
        #stroka += item
        a = 1
    else:
        #stroka += item
        if a == 1:
            Anton.append(item)
        else:
            Valya.append(item)
print(len(Valya))
print(len(Anton))
V = set()
z = ''
for item in Valya:
    z += item

V.add(z)

print(V)

