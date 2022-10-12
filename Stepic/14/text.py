with open('text.txt', 'r', encoding='utf-8') as file:
    list1 = file.readline()

s = ''
for i in range(len(list1) - 1, -1, -1):
    s = s + list1[i]

print(s)
