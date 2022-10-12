with open('lines.txt', 'r', encoding='utf-8') as file:
    list1 = file.readlines()

maximum = 0
for i in range(len(list1)):
    if len(list1[i]) > maximum:
        maximum = len(list1[i])
    item = list1[i].split('\n')
    # print(item[0])

for j in range(len(list1)):
    if len(list1[j]) == maximum:
        print(list1[j], end='')
    else:
        pass
