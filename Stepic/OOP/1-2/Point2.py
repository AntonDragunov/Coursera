# здесь объявляется класс Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        obj = Point(self.x, self.y)
        return obj


pt = Point(10, 12)
pt_clone = pt.clone()
