import math
from fractions import Fraction

n = int(input())
l = []
a = n / 2
i = 1
while i < a:
    #print(i, n - i)
    l.append(str(Fraction(i, (n - i))))

    i += 1
#print(l)
# print(max(l))
j = 0
maximum = 0
if len(l) != 1:
    while j < len(l):
        if Fraction(l[j]) >= Fraction(maximum) and Fraction(l[j]).numerator + Fraction(l[j]).denominator == n:
            maximum = l[j]
        else:
            pass
        j += 1
else:
    maximum = Fraction(l[0])

# for item in l:
#     if item >= max
print(maximum)
