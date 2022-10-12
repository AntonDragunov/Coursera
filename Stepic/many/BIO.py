n = set(map(int, input().split()))
m = set(map(int, input().split()))
p = set(map(int, input().split()))
all_get_scores = n | m | p
all_scores = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}



all_scores.difference_update(all_get_scores)
a = sorted(all_scores)
print(*a)
