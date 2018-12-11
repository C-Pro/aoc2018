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
Step G must be finished before step E can begin.
Step H must be finished before step G can begin.
Step C must be finished before step K can begin.
Step C must be finished before step J can begin.
Step C must be finished before step I can begin.
'''
        text = f.read()

    steps = []
    distinct = set([])

    for line in text.splitlines():
        m = p.match(line.strip())

        a = m.group(1)
        b = m.group(2)
        distinct.add(a)
        distinct.add(b)
        steps.append((a, b))

    n = max([I(x) for x in distinct])+1

    steps.sort(key=lambda x: "{}{}".format(x[0], x[1]))

    dep = [x[1] for x in steps]
    start = sorted(set([x[0] for x in steps if x[0] not in dep]))
    seq = start[:]
    seq = []
    stepsc = steps[:]
    while len(steps) > 0:
        a, b = steps[0]
        steps = steps[1:]
        i = find(seq, b)
        if i >= 0:
            ai = find(seq, a)
            bi = find(seq, b)
            if ai < 0:
                seq.insert(i, a)
            elif ai > bi:
                seq[ai], seq[bi] = seq[bi], seq[ai]
            continue
        if find(seq, a) >= 0:
            seq.append(b)
        else:
            seq += [a, b]

    print("".join(seq))
    import random

    for i in range(1000):
        (a, b) = random.choice(stepsc)
        ai = find(seq, a)
        bi = find(seq, b)
        if ai > bi:
            seq[ai], seq[bi] = seq[bi], seq[ai]
    print("".join(seq))
    print(len(seq))
