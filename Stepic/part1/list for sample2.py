n = int(input())
my_list = []
list1 = []
j = 1

for i in range(n + 1):
    while j <= i:
        list1.append(j)
        print(list1)
        j += 1
    my_list.append(list1)
