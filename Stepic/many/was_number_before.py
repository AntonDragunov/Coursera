n = list(map(int, input().split()))
unic_numbers = set()

for item in n:
    if item in unic_numbers:
        print('YES')
        unic_numbers.add(item)
    else:
        print("NO")
        unic_numbers.add(item)
