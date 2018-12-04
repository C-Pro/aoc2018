import os

v = 0
with open('input.txt', 'r') as f:
    text = f.read()
    for line in text.splitlines():
        #if len(line.strip()) == 0:
        #    continue
        f = '{}+({})'.format(v, line)
        v = eval(f)
        print(f, '=', v)

