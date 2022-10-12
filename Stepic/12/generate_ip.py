import random








def generate_ip():
    a = ''
    for i in range(4):
        b = random.randint(0,255)
        a = a + str(b) + '.'

    return (a[:-1])

generate_ip()