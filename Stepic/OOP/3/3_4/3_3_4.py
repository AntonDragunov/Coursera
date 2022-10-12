class NewList:

    def __init__(self, list1=[]):
        self.list1 = list1

    def __sub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise ArithmeticError("Правый операнд должен быть типом int или объектом Clock")

        sc = other if isinstance(other, list) else other.list1


        #return NewList(self.list1 + sc)

        for i in sc:
            self.list1.remove(i) if i in self.list1 else None


        #a = list(lambda x: self.list1.remove(x) if x in self.list1 else None, sc)

        return self.list1

    def __rsub__(self, other):
        return self + other

    def __isub__(self, other):
        pass

    def get_list(self):
        return self.list1


lst = NewList()  # пустой список
lst = NewList([-1, 0, 7.56, True])  # список с начальными значениями

lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
