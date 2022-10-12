from random import random, choice

list1 = []
file = open('lines.txt', 'r', encoding='utf-8')
for line in file:
    list1.append(line)
#print(type(list1))

print(choice(list1))
#print(list1)
file.close()
