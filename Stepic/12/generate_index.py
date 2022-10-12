import random


def generate_index():
    a = ''
    for i in range(2):
        a = a + str(chr(random.randint(65, 90)))
    a = a + str(random.randint(0, 99)) + '_'
    a = a + str(random.randint(0, 99))
    a = a + str(chr(random.randint(65, 90)))
    a = a + str(chr(random.randint(65, 90)))
    return a


print(generate_index())
