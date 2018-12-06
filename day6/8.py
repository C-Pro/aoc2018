import numpy as np

SIZE = 400
a = np.full((SIZE, SIZE), -1, dtype=np.int8)

coords = []

with open('input.txt', 'r') as f:
    text = '''1, 1
1, 6
8, 3
3, 4
5, 5
8, 9'''
    text = f.read()
    i = 1
    for line in text.splitlines():
        x, y = line.split(",")
        x = int(x)
        y = int(y)
        a[x, y] = i
        i += 1
        coords.append((x, y))

    for x in range(0, SIZE):
        for y in range(0, SIZE):
            min_dist = SIZE
            min_i = None
            cnt = {}
            for i in range(len(coords)):
                _x, _y = coords[i]
                dist = abs(x-_x) + abs(y-_y)

                if dist in cnt.keys():
                    cnt[dist] += 1
                else:
                    cnt[dist] = 1

                if dist < min_dist:
                    min_dist = dist
                    min_i = i
            if cnt[min_dist] == 1:
                a[x, y] = min_i
            else:
                a[x, y] = -1

    bad = set([-1])
    for x in range(0, SIZE):
        bad.add(a[x, 0])
        bad.add(a[0, x])
        bad.add(a[x, SIZE-1])
        bad.add(a[SIZE-1, x])

    counts = [0] * len(coords)
    for x in range(0, SIZE):
        for y in range(0, SIZE):
            if a[x, y] not in bad:
                counts[a[x, y]] += 1

    print(max(counts))
