def root(*points):
    perimeter = 0
    for i in range(len(points)):
        x1, y1 = points[i]
        if i+1 == len(points):
            i = -1
        x2, y2 = points[i + 1]
        perimeter += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print(round(perimeter, 1))

a = (2, 0)
b = (-4, 5)
c = (4, 10)
d = (8, 7)
e = (4, 5)

root(a, b, c, d, e)