from decimal import *


n = Decimal(input())


result = n.exp() + n.ln() + n.log10() + n.sqrt()

print(result)
