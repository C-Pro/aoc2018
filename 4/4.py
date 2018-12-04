import numpy as np
import re

p = re.compile('#([0-9]+)\s*@\s*([0-9]+),([0-9]+)\s*:\s*([0-9]+)\s*x\s*([0-9]+)')
a = np.zeros((2000,2000), dtype=np.uint16)

def mark(line):
    m = p.match(line)
    offX = int(m.group(2))
    offY = int(m.group(3))
    width = int(m.group(4))
    height = int(m.group(5))
    for x in range(offX + 1, offX + 1 + width):
        for y in range(offY + 1, offY + 1 + height):
            a[x][y] = a[x][y] + 1

with open('input.txt', 'r') as f:
    text = f.read()
    for line in text.splitlines():
        mark(line)
    print((a>1).sum())

