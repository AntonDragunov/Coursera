file = open('numbers.txt', 'r', encoding='utf-8')

result = file.readlines()

for item in result:
    a = 0
    g = item.split()
    for _ in g:
        a += int(_)
    print(a)
