n = list(map(int, input().split()))

count = 0
for i in range(len(n)-1):
    if int(n[i+1]) > int(n[i]):
        count += 1
    else:
        pass

print(count)
