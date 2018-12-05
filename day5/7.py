
from collections import deque


def conv(text):
    newtext = deque(maxlen=len(text))
    for c in text:
        if len(newtext) > 0:
            if abs(ord(c) - ord(newtext[-1])) == 32:
                newtext.pop()
                continue
        newtext.append(c)
    return "".join(newtext)


with open('input.txt', 'r') as f:
    text = f.read().strip()
    #text = "dabAcCaCBAcCcaDA"

    # part1
    print(len(conv(text)))

    # part2
    units = set(list(text.lower()))

    min_len = len(text)
    worst_unit = None
    for unit in units:
        newtext = [c for c in text if c.lower() != unit]
        new_len = len(conv(newtext))
        if new_len < min_len:
            min_len = new_len
            worst_unit = unit

    print(worst_unit)
    print(min_len)
