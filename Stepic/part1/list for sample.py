n = int(input())
my_list = []
list1 = []
j = 1
while j <= n:
    list1.append(j)
    j += 1

my_list = [list1 for _ in range(n)]
for item in my_list:
    print(item)

