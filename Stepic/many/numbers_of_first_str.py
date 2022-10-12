n = set(map(int, input().split()))
m = set(map(int, input().split()))

z = n.difference(m)

a = sorted(z)
print(*a)
