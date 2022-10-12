s = []

file = open('nums.txt', 'r', encoding='utf-8')

result = file.read()
#print(result)

s = result.split()
a = 0
#print(result)

for item in s:
    a += int(item)

print(a)
file.close()
