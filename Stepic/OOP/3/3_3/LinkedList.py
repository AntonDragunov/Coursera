class ObjList:

    def __init__(self, data):
        self.__data = ""
        self.data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) == str:
            self.__data = value


    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        self.__prev = obj


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if not self.head:
            self.head = obj

    # def remove_obj(self, indx):
    #
    #     if self.tail is None:
    #         return
    #     prev = self.tail.set_prev()
    #     if prev:
    #         prev.set_next(None)
    #     self.tail = prev
    #     if self.tail is None:
    #         self.head = None

    def __len__(self, linked_lst):
        s = []
        h = self.head
        while h:
            s.append(h.get_data())
            h = h.set_next()
        return len(s)


    def linked_lst(self, indx):
        return


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
s = linked_lst(1) # s = Balakirev