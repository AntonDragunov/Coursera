abscissas = list(map(float, input().split()))
ordinates = list(map(float, input().split()))
applicates = list(map(float, input().split()))

for x, y, z in zip(abscissas, ordinates, applicates):


    result = all(map(lambda r2:  True if int(x ** 2 + y ** 2 + z ** 2) <= 4 else False, zip(abscissas, ordinates, applicates)))


print(result)



#0.0 1.0 2.0
#0.0 0.0 1.1
#0.0 1.0 1.5