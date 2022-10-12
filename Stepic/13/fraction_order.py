import math
from fractions import Fraction

n = int(input())
l = []
a = n / 2
i = 1
j = 2
while i < n:
    while j <= n:
        #print(i, j)
        if i != j and i % j !=0 and i < j:
            l.append((Fraction(i, j)))
        else:
            pass
        j += 1
    i += 1
    j = 2

l = list(set(l))
#print(l)
l = sorted(l)
#print(l)
for item in l:
    print(item)

