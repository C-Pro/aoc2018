import numpy as np

SIZE = 400
coords = []
MAXDIST = 10000

with open('input.txt', 'r') as f:
    text = '''1, 1
1, 6
8, 3
3, 4
5, 5
8, 9'''
    text = f.read()
    for line in text.splitlines():
        x, y = line.split(",")
        x = int(x)
        y = int(y)
        coords.append((x, y))

    cnt = 0
    for x in range(0, SIZE):
        for y in range(0, SIZE):
            min_dist = SIZE
            min_i = None
            sum_coords = 0
            for i in range(len(coords)):
                _x, _y = coords[i]
                dist = abs(x-_x) + abs(y-_y)
                sum_coords += dist
            if sum_coords < MAXDIST:
                cnt += 1
    print(cnt)
