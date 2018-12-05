import numpy as np
import re
import time

ids = {}
p = re.compile('\[([^\]]+)\]\s+(.+)')
pid = re.compile('.+#([0-9]+) begins shift')

log = []


with open('input.txt', 'r') as f:
    text = f.read()
    for line in text.splitlines():
        m = p.match(line)
        log.append((time.strptime(m.group(1), "1518-%m-%d %H:%M"), m.group(2)))
    log = sorted(log, key=lambda x: x[0])
    for l in log:
        print(time.strftime("%Y-%m-%d %H:%M", l[0]), l[1])

    sec = {}
    starttime = None
    id = None
    for line in log:
        ts = line[0]
        m = pid.match(line[1])
        if m:
            id = int(m.group(1))
            if id not in sec.keys():
                sec[id] = [0]*60
            startime = None
            print("#{} started".format(id))
        if line[1].strip().startswith("falls"):
            starttime = int(time.strftime("%M", ts))
        if line[1].strip().startswith("wake"):
            endtime = int(time.strftime("%M", ts))
            for minute in range(starttime, endtime):
                sec[id][minute] += 1

    gs = 0 #sum
    gi = 0 #id
    gm = 0 #minute
    coolguy = None
    for k, v in sec.items():
        #part2
        for minute, msum in enumerate(v):
            if msum > gs:
                gs = msum
                gm = minute
                gi = k
        #end part2

        if coolguy:
            if coolguy["sum"] < sum(v):
                coolguy = {"sum": sum(v),
                           "id": k,
                           "minutes": v}
        else:
            coolguy = {"sum": sum(v),
                       "id": k,
                       "minutes": v}
    print(coolguy)
    maxsum = 0
    maxmin = 0
    for i in range(0,60):
        if coolguy["minutes"][i] > maxsum:
            maxsum = coolguy["minutes"][i]
            maxmin = i
    print("Part1")
    print(maxmin*coolguy["id"])
    print("Part2")
    print(gi*gm)
    
