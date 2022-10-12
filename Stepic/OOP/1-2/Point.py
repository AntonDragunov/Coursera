class Point:
    def __init__(self, x, y, color = 'black'):
        self.x = x
        self.y = y
        self.color = color
        #print(str(self))

# p1 = Point(10, 20)
# p2 = Point(12, 5, 'red')
points = []
i = 0
z = 0
while i <= 3000:
    if z != 1000:
        if i == 2:
            p = Point(i+1, i+1, 'yellow')
        else:
            p = Point(i+1, i+1)
        i +=2
        z +=1

        points.append(p)
        print(p.__dict__, z)
    else:
        break







