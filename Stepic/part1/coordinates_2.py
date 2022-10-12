points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]


def distance(point):
    s = 0
    for i in range(len(point)):
        s = (point[0]) ** 2 + (point[1]) ** 2

    return s


print(sorted(points, key=distance))
