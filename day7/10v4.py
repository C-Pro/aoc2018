import re


def I(char):
    return ord(char)-ord('A')


def A(i):
    return chr(ord('A') + i)


def find(l, v):
    i = -1
    try:
        i = l.index(v)
    except ValueError:
        i = -1
    return i


steps = []
distinct = set([])


def canput(x, seq):
    for a in [s[0] for s in steps if s[1] == x]:
        if a not in seq:
            return False
    return True


if __name__ == "__main__":

    p = re.compile('Step ([A-Z]{1}).+step ([A-Z]{1}) can begin.')

    with open('input.txt', 'r') as f:
        text = '''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
'''
        text = f.read()

    for line in text.splitlines():
        m = p.match(line.strip())

        a = m.group(1)
        b = m.group(2)
        distinct.add(a)
        distinct.add(b)
        steps.append((a, b))

    seq = []
    while len(distinct) > 0:
        nextC = min(sorted([c for c in distinct if canput(c, seq)]))
        seq += nextC
        distinct.remove(nextC)
    print("".join(seq))
