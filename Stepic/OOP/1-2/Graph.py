class Graph:

    def set_data(self, data):
        self.data = data

    def draw(self):
        LIMIT_Y = [c for c in range(0, 11)]
        a = [i for i in self.data if i in LIMIT_Y]
        return print(*a)

graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()
