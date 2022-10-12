n = set(map(int, input().split()))
m = set(map(int, input().split()))
p = set(map(int, input().split()))




two_pupils = n | m



p.difference_update(two_pupils)
a = sorted(p, reverse=True)
print(*a)
