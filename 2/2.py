import os

v = 0
m = {0: True}
with open('input.txt', 'r') as f:
    text = f.read()
    while True:
        for line in text.splitlines():
            #if len(line.strip()) == 0:
            #    continue
            f = '{}+({})'.format(v, line)
            v = int(eval(f))
            if m.get(v, False):
                print(v)
                exit()
            #print(v, m.get(v, False))
            m[v] = True


