import re
import numpy as np


def I(char):
    return ord(char)-ord('A')


def A(i):
    return chr(ord('A') + i)

# for char in ['A','B','C','X','Y','Z']:
#    print(A(I(char)))


def walk(seq):
    seqs = []

    while True:
        added = False
        y = I(seq[-1])
        for x in range(n-1, -1, -1):
            if ind[x, y] == 1:
                seq += A(x)
                added = True
                seqs = seqs + walk(seq)

        if not added:
            break
    seqs.append(seq)
    seqs = list(set(["".join(x) for x in seqs]))
    return seqs


def merge(seq1, seq2):
    ret = ""
    if len(seq1) > len(seq2):
        seq1, seq2 = seq2, seq1
    i = 0
    for c in seq1:
        while i < len(seq2) and c > seq2[i]:
            ret += seq2[i]
            i += 1
        if i == len(seq2) or c != seq2[i]:
            ret += c
    if i == len(seq2):
        return ret
    return ret + seq2[i:]


if __name__ == "__main__":

    p = re.compile('Step ([A-Z]{1}).+step ([A-Z]{1}) can begin.')

    with open('input.txt', 'r') as f:
        text = '''Step C must be finished before step A can begin.
    Step C must be finished before step F can begin.
    Step A must be finished before step B can begin.
    Step A must be finished before step D can begin.
    Step B must be finished before step E can begin.
    Step D must be finished before step E can begin.
    Step C must be finished before step G can begin.
    Step F must be finished before step E can begin.
    Step H must be finished before step E can begin.
    Step I must be finished before step H can begin.
    Step J must be finished before step I can begin.'''
        #text = f.read()

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
        ind = np.zeros((n, n), dtype=np.uint8)

        for (a, b) in [(I(x[0]), I(x[1])) for x in steps]:
            ind[a, b] = 1
        print(ind)

        leaves = np.where(~ind.any(axis=1))[0]

        seqs = []
        for leaf in leaves:
            seqs += walk([A(leaf)])

        print(seqs)
        seq = seqs[0]
        for next_seq in seqs[1:]:
            seq = merge(seq, next_seq)
        print(seq)
        print(len(seq))
        print(len(distinct))
