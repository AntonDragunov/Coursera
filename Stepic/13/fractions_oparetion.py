from fractions import Fraction

m = str(input())

n = str(input())


print(m + ' + ' + n + ' = ' + str((Fraction(m) + (Fraction(n)))))
print(m + ' - ' + n + ' = ' + str((Fraction(m) - (Fraction(n)))))
print(m + ' * ' + n + ' = ' + str((Fraction(m) * (Fraction(n)))))
print(m + ' / ' + n + ' = ' + str((Fraction(m) / (Fraction(n)))))