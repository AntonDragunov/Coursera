import sys


class ListObject:
    def __init__(self, data):
        self.next_obj = None
        self.data = data

    def link(self, obj):
        self.next_obj = obj


lst_in = list(map(str.strip, sys.stdin.readlines()))


head_obj = ListObject(lst_in[0])

obj = head_obj

for i in range(1, len(lst_in)):
    obj_new = ListObject(lst_in[i])
    obj.link(obj_new)
    obj = obj_new
