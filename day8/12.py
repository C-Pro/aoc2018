import os


def parse(numbers, i=0):
    num_children = numbers[i]
    num_meta = numbers[i+1]
    sum_meta = 0
    i += 2
    ch_meta = {}
    for ch in range(num_children):
        i, child_meta = parse(numbers, i)
        ch_meta[ch+1] = child_meta
    if num_children == 0:
        for m in range(i, i + num_meta):
            sum_meta += numbers[m]
    else:
        for m in range(i, i + num_meta):
            sum_meta += ch_meta.get(numbers[m], 0)
    return max([m, i])+1, sum_meta


PROD = True

with open('input.txt', 'r') as f:
    text = f.read()
    if not PROD:
        text = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
    numbers = [int(x) for x in text.split()]
    print(parse(numbers)[1])
