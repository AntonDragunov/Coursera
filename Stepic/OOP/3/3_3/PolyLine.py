class PolyLine:

    def __init__(self, *args):
        self.line = [x for x in args]

    def add_coord(self, x, y):
        self.line.append((x, y))

    def remove_coord(self, indx):
        self.line.pop(indx)

    def get_coords(self):
        return self.line
