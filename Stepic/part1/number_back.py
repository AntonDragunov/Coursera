i = 1
a = int(input())
c = str(a)
if len(c) == 6:
    d = c[1:6]

    b = ''
    while i < (len(d)+1):
        b += (d[-i])
        i += 1
    e = c[:1] + b
    e = e.lstrip('0')
    print(int(e))
else:
    d = c[:6]

    b = ''
    while i <= len(d):
        b += (d[-i])
        i += 1

    b = b.lstrip('0')
    print(int(b))
