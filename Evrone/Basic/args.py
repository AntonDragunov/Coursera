def multiply(*mult):
    result = 1
    for n in mult:
        result *= n
    return result


print(multiply(1, 2, 3, 4))
