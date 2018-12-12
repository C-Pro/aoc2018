import re


def I(char):
    return ord(char)-ord('A')+1


PROD = True

MINTIME = 0
WORKERS = 2

if PROD:
    MINTIME = 60
    WORKERS = 5


steps = []
distinct = set([])
workers = [{"Working": 0, "Task": None} for _ in range(0, WORKERS)]


def tick():
    tasks = []
    for worker in workers:
        if worker["Task"]:
            worker["Working"] += 1
            if worker["Working"] == I(worker["Task"]) + MINTIME:
                task = worker["Task"]
                worker["Task"] = None
                worker["Working"] = 0
                tasks += task
    # print(workers)
    return tasks


def getFree():
    for i in range(0, len(workers)):
        if workers[i]["Task"] == None:
            return i
    return None


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
        if PROD:
            text = f.read()

    for line in text.splitlines():
        m = p.match(line.strip())

        a = m.group(1)
        b = m.group(2)
        distinct.add(a)
        distinct.add(b)
        steps.append((a, b))

    seq = []
    seqWorkers = []
    second = 0
    while len(distinct) > 0:
        notused = distinct.difference(seqWorkers)
        validmoves = [c for c in notused if canput(c, seqWorkers)]
        nextC = None
        if len(validmoves) > 0:
            nextC = min(validmoves)
        if nextC is None:
            c = tick()
            second += 1
            if len(c) > 0:
                seqWorkers += c
            continue

        i = None
        while True:
            i = getFree()
            if i is not None:
                break
            c = tick()
            second += 1
            if len(c) > 0:
                seqWorkers += c

        workers[i]["Task"] = nextC
        workers[i]["Working"] = 0
        seq += nextC

        distinct.remove(nextC)

    while True:
        working = False
        for i in range(0, WORKERS):
            if workers[i]["Task"]:
                working = True
        if not working:
            break

        c = tick()
        second += 1
        if len(c) > 0:
            seqWorkers += c

    print("".join(seq))
    print("".join(seqWorkers))
    print(second)
