numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34),
           (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4),
           (90, 1, -45, -21)]




def compare_by_avg(number):
    s = 0
    l = 0
    for i in range(len(number)):
        if len(number) !=0:
            s += number[i]
            #print(number, s, i)

        else:
            return l
    #print(number, s / (i + 1))
    return s / (i+1)

print(max(numbers, key=compare_by_avg))
print(min(numbers, key=compare_by_avg))