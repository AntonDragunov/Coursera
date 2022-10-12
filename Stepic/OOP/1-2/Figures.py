import random
from random import choice


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = []
numbers = [i for i in range(100)]
for i in range(217):
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    c = random.randint(0, 100)
    d = random.randint(0, 100)
    # print(a, b, c, d)
    s = random.randint(0, 2)
    if s == 1:
        s = Line(a, b, c, d)
    elif s == 2:
        s = Rect(a, b, c, d)
    else:
        s = Ellipse(a, b, c, d)
    elements.append(s)
    #print(s.__dict__, type(s))
# print()
for i in range(217):
    #print(elements[i].__dict__, i)
    if isinstance(elements[i], Line):
        m = Line(0, 0, 0, 0)
        elements.insert(i, m)
        elements.pop(i+1)

    else:
        pass
# for _ in elements:
#     print(_.__dict__, type(_))