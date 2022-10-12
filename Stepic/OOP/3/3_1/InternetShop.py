class Shop:

    def __init__(self, title):
        self.goods = []
        self.title = title


    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    __isinstance = 1
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.id = Product.__isinstance
        Product.__isinstance += 1

    def __setattr__(self, key, value):
        if key == 'id':
            if type(value) != int or value <= 0:
                raise TypeError("Неверный тип присваиваемых данных.")
            object.__setattr__(self, key, value)
        elif key == 'name':
            if type(value) != str:
                raise TypeError("Неверный тип присваиваемых данных.")
            object.__setattr__(self, key, value)
        elif key == 'weight' or key == 'price':
            if not type(value) in (int, float) or value <=0:
                raise TypeError("Неверный тип присваиваемых данных.")
            object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")

shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")

del book.id
