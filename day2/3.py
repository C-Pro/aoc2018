import os

c = {2: 0, 3: 0}
with open('input.txt', 'r') as f:
    text = f.read()
    for line in text.splitlines():
        chars = {}
        for char in line:
            if char not in chars:
                chars[char] = 0
            chars[char] += 1
        c2 = False
        c3 = False
        for (char, count) in chars.items():
            if count == 3:
                c3 = True
            if count == 2:
                c2 = True
        if c2:
            c[2] += 1
        if c3:
            c[3] += 1
    print(c[2]*c[3])
