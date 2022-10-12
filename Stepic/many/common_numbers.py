n = set(map(int, input().split()))
m = set(map(int, input().split()))

n.intersection_update(m)
a = sorted(n)
print(*a)