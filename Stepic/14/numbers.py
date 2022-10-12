s = 0

file = open('numbers.txt', 'r', encoding='utf-8')
for line in file:
    s += int(line)

print(s)

file.close()
