from fractions import Fraction

n = int(input())
s = 0
i = 1
while i <= n:
    s += Fraction(1, i ** 2)
    i += 1

print(s)
