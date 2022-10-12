a = int(input())
b = int(input())



numbers = [int(i) for i in range(a, b + 1) if '0' not in str(i)]
result = []
for i in numbers:
    if all(i % int(x) == 0 for x in str(i)):
        result.append(i)

print(*result)
