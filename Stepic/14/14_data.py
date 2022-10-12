with open('data.txt', 'r', encoding='utf-8') as file:
    list1 = file.readlines()

for i in range(len(list1) - 1, -1, -1):
    item = list1[i].split('\n')
    print(item[0])
