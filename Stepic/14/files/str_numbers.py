with open('input.txt', 'r', encoding='utf-8') as file:
    list1 = file.readlines()

with open('output.txt', 'w+', encoding='utf-8') as file:
    for item in enumerate(list1):
        print(item[0]+1, ') ', sep='', end='', file=file)
        print(item[1], end='', file=file)
