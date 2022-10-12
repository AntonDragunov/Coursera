n = set(map(int, input().split()))
m = set(map(int, input().split()))
p = set(map(int, input().split()))




all_score = n | m | p

same = n & m & p


all_score.difference_update(same)
a = sorted(all_score)
print(*a)

