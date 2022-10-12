n = set(map(int, input().split()))
m = set(map(int, input().split()))

n.intersection_update(m)
print(len(n))
