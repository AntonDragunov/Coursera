def func_apply(function, items):
    acc = []
    for item in items:
        acc.append(function(item))
    return acc

def add3(x):
    return x + 3


def mul7(x):
    return x * 7


print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
print(func_apply(str, [1, 2, 3, 4, 5, 6]))