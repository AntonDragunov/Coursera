n = str(input())
list1 = []
file = open(n)
for line in file:
    list1.append(line)
#print(*list1)
#print()
print(list1[-2])
file.close()
