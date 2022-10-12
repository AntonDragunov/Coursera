file = open('prices.txt', 'r', encoding='utf-8')

prices = file.readlines()
list1 = []
item1 = []

for item in prices:
    item = item.rstrip()
    item1 = item.split('\t')

    list1.append(item1)
result = 0

for item in list1:
    result += int(item[1]) * int(item[2])

print(result)

file.close()
