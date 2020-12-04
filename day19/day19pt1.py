import re

PROD = True


r = re.compile(r"^[^0-9]+([0-9]+)$")
cre = re.compile(r"^([a-z]+)[\s]+([0-9]+)[\s]+([0-9]+)[\s]+([0-9]+)$")

regs = [0] * 6


def call(op, a, b, c):
    if op == "seti":
        regs[c] = a
    elif op == "setr":
        regs[c] = regs[a]
    elif op == "addi":
        regs[c] = regs[a] + b
    elif op == "addr":
        regs[c] = regs[a] + regs[b]
    elif op == "muli":
        regs[c] = regs[a] * b
    elif op == "mulr":
        regs[c] = regs[a] * regs[b]
    elif op == "bani":
        regs[c] = regs[a] & b
    elif op == "banr":
        regs[c] = regs[a] & regs[b]
    elif op == "bori":
        regs[c] = regs[a] | b
    elif op == "borr":
        regs[c] = regs[a] | regs[b]
    elif op == "gtir":
        regs[c] = 1 if a > regs[b] else 0
    elif op == "gtri":
        regs[c] = 1 if regs[a] > b else 0
    elif op == "gtrr":
        regs[c] = 1 if regs[a] > regs[b] else 0
    elif op == "eqir":
        regs[c] = 1 if a == regs[b] else 0
    elif op == "eqri":
        regs[c] = 1 if regs[a] == b else 0
    elif op == "eqrr":
        regs[c] = 1 if regs[a] == regs[b] else 0


def step(prog):
    if regs[ip] >= len(prog):
        return False
    s = "ip={} ".format(regs[ip]) + str(regs)
    op, a, b, c = prog[regs[ip]]
    s += " {} {} {} {} ".format(op, a, b, c)
    call(op, a, b, c)
    s += str(regs)
    if not PROD:
        print(s)
    return True


with open("input.txt") as f:
    text = f.read().splitlines()
    if not PROD:
        text = """# ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5""".splitlines()

    ip = int(r.match(text[0]).group(1))

    prog = []
    for l in text[1:]:
        m = cre.match(l)
        prog.append((m.group(1), int(m.group(2)),
                     int(m.group(3)), int(m.group(4))))

    while step(prog):
        regs[ip] += 1

    print(regs[0])
'''
EXPECT:
ip=0 [0, 0, 0, 0, 0, 0] seti 5 0 1 [0, 5, 0, 0, 0, 0]
ip=1 [1, 5, 0, 0, 0, 0] seti 6 0 2 [1, 5, 6, 0, 0, 0]
ip=2 [2, 5, 6, 0, 0, 0] addi 0 1 0 [3, 5, 6, 0, 0, 0]
ip=4 [4, 5, 6, 0, 0, 0] setr 1 0 0 [5, 5, 6, 0, 0, 0]
ip=6 [6, 5, 6, 0, 0, 0] seti 9 0 5 [6, 5, 6, 0, 0, 9]
'''
