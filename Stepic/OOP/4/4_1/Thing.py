class Thing:
    __isinstance_id = 0
    __attrs = ("id", 'name', 'price', 'weight', 'dims', 'memory', 'frm')

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = self.__get_id()
        self.weight = self.dims = self.memory = self.frm = None

    @classmethod
    def __get_id(cls):
        Thing.__isinstance_id += 1
        return Thing.__isinstance_id

    def get_data(self):
        return tuple(getattr(self, name) for name in self.__attrs)


class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm


table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())
