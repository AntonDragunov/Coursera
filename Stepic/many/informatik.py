n = set(map(str, input().split()))
m = set(map(str, input().split()))
p = set(map(str, input().split()))

n.intersection_update(m)

n.difference_update(p)

print(*n)

