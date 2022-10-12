class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.gd = gd
        self.goods.append(self.gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        print([f'{g.name}: {g.price}' for g in self.goods])

class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()

cart.add(TV('ТВ1', 1000))
cart.add(TV('ТВ2', 10000))
cart.add(Table('столик1', 2000))
cart.add(Notebook('ноут1', 23000))
cart.add(Notebook('ноут2', 27000))
cart.add(Cup('кружка', 100))
cart.get_list()