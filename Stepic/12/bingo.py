import random

bingo = []
number = []
number2 = []
chisla = list(range(1, 76))
number = random.sample(chisla, 25)
#print(number)
number.insert(12, 0)
#print(number)
number.pop()
#print(number)
z = 0
for i in range(5):
    number2 = []
    for j in range(5):
        number2.append(number[z])
        #print(z, number2)
        z += 1
    #print(z, number2)
    bingo.append(number2)

for item in bingo:
    for j in item:
        print(str(j).ljust(3), end='')
    print()
