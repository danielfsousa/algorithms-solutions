def convex_hull(a, b, c):
    area2 = (b['x'] - a['x']) * (c['y'] - a['y']) - (b['y'] - a['y']) * (c['x'] - a['x'])
    if area2 < 0:
        return -1
    elif area2 > 0:
        return 1
    else:
        return 0


points = [{'x': 2.0, 'y': 2.0},
          {'x': 2.0, 'y': 3.0},
          {'x': 3.0, 'y': 2.0}]

print(convex_hull(*points))
