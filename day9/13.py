import re


class Circle(object):
    def __init__(self):
        self.ringbuf = []
        self.curr_marble = 0
        self.curr_marble_idx = 0

    def _get_index(self, offset):
        return (self.curr_marble_idx + offset) % len(self.ringbuf)

    def insert(self, marble):
        if marble % 23 == 0 and marble > 0:
            grab = self.ringbuf[self._get_index(-7)]
            self.curr_marble = self.ringbuf[self._get_index(-6)]
            self.ringbuf.remove(grab)
            self.curr_marble_idx = self.ringbuf.index(self.curr_marble)
            return marble + grab
        if marble == 0:
            self.ringbuf.append(marble)
        else:
            i = self._get_index(+2)
            self.ringbuf.insert(i, marble)
            self.curr_marble_idx = i
        self.curr_marble = marble
        return 0


def play(np, nm):
    players = [0] * np
    board = Circle()
    for marble in range(nm+1):
        players[(marble-1) % np] += board.insert(marble)
    return max(players)


p = re.compile('([0-9]+)[^0-9]+([0-9]+).+')

tests = [
    ("10 players; last marble is worth 1618 points", 8317),
    ("13 players; last marble is worth 7999 points", 146373),
    ("17 players; last marble is worth 1104 points", 2764),
    ("21 players; last marble is worth 6111 points", 54718),
    ("30 players; last marble is worth 5807 points", 37305),
    ("428 players; last marble is worth 72061 points", 409832),
]

for t in tests:
    m = p.match(t[0])
    playersN = int(m.group(1))
    marblesN = int(m.group(2))
    res = play(playersN, marblesN)
    if res != t[1]:
        print("Fail: play({},{})={}, expected {}".format(
            playersN, marblesN, res, t[1]))
