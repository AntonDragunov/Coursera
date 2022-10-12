def greet(a, *args):
    s = 'Hello, '
    if len(args) != 0:
        s = s + a + ' And '
        m = 0
        for i in args:
            m = m + 1
            s = s + i

            if m == len(args):
                pass
            else:
                s = s + ' And '
        s = s + '!'
    else:
        s = s + a + '!'

    return s
greet('Timur', 'Roman')