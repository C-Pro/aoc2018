import re


steps = []
distinct = set([])


def less(a, b):
    if _lt(a, b):
        return True
    if _lt(b, a):
        return False
    return a < b


def _lt(a, b):
    print(a, b)
    for x, y in steps:
        if (a, b) == (x, y):
            return True
        if (a, b) == (y, x):
            return False
    for x, y in steps:
        if a == x:
            if _lt(y, b):
                return True
    return None


tests = [([], 'A', 'B', True),
         ([], 'B', 'A', False),
         ([], 'A', 'Z', True),
         ([], 'X', 'B', False),
         ([('Z', 'A')], 'A', 'Z', False),
         ([('Z', 'A')], 'Z', 'A', True),
         ([('Z', 'A'), ('B', 'Z')], 'B', 'A', True),
         ([('Z', 'A'), ('B', 'Z')], 'A', 'B', False),
         ([('Z', 'A'), ('B', 'A')], 'A', 'B', False),
         ([('Z', 'A'), ('B', 'A')], 'A', 'Z', False),
         ([('Z', 'A'), ('B', 'A')], 'B', 'Z', True),
         ([('Z', 'A'), ('B', 'A')], 'Z', 'B', False),
         ([('Z', 'A'), ('B', 'A'), ('A', 'C')], 'Z', 'B', False),
         ]


for t in tests:
    steps = t[0]
    if less(t[1], t[2]) != t[3]:
        print("{}: less({},{}) = {}. Expected {}.".format(t[0],
                                                          t[1], t[2], less(t[1], t[2]), t[3]))
        exit(1)

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
        #text = f.read()

    for line in text.splitlines():
        m = p.match(line.strip())

        a = m.group(1)
        b = m.group(2)
        distinct.add(a)
        distinct.add(b)
        steps.append((a, b))

    seq = [x for x in distinct]
    for i in range(0, len(seq)):
        for j in range(0, len(seq)):
            if i == j:
                continue
            a = seq[i]
            b = seq[j]
            if less(b, a):
                seq[i] = b
                seq[j] = a
    print("".join(seq))
