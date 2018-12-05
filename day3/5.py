import numpy as np
import re

ids = {}
p = re.compile('#([0-9]+)\s*@\s*([0-9]+),([0-9]+)\s*:\s*([0-9]+)\s*x\s*([0-9]+)')
a = np.zeros((2000,2000), dtype=np.uint16)

def mark(line):
    global ids
    m = p.match(line)
    id = int(m.group(1))

    offX = int(m.group(2))
    offY = int(m.group(3))
    width = int(m.group(4))
    height = int(m.group(5))
    overlaps = False
    for x in range(offX + 1, offX + 1 + width):
        for y in range(offY + 1, offY + 1 + height):
            if a[x][y] > 0:
                overlaps = True
                try:
                    del ids[a[x][y]]
                except:
                    None
            else:
                a[x][y] = id
    if not overlaps:
        ids[id] = True

with open('input.txt', 'r') as f:
    text = f.read()
    for line in text.splitlines():
        mark(line)
    print(ids)

