import sys
input = sys.stdin.readline


class Tree:
    def __init__(self, ys):
        self.ys = ys
        self.n = len(ys) - 1
        self.cover = [0] * (4 * self.n)
        self.length = [0] * (4 * self.n)

    def update(self, node, l, r, ql, qr, diff):
        if qr <= l or ql >= r:
            return

        if ql <= l and qr >= r:
            self.cover[node] += diff

        else:
            mid = (l + r) // 2
            self.update(node * 2, l, mid, ql, qr, diff)
            self.update(node * 2 + 1, mid, r, ql, qr, diff)

        if self.cover[node] > 0:
            self.length[node] = self.ys[r] - self.ys[l]

        else:
            self.length[node] = 0 if l + \
                1 == r else self.length[node * 2] + self.length[node * 2 + 1]


n = int(input())
rects = [tuple(map(int, input().split())) for _ in range(n)]

ys = set()
for _, _, y1, y2 in rects:
    ys.add(y1)
    ys.add(y2)

ys = sorted(ys)
y_index = {v: i for i, v in enumerate(ys)}

events = []
for x1, x2, y1, y2 in rects:
    events.append((x1, 1, y1, y2))
    events.append((x2, -1, y1, y2))

events.sort()

tree = Tree(ys)
prev_x = events[0][0]
area = 0

i = 0
while i < len(events):
    x = events[i][0]
    dx = x - prev_x
    area += dx * tree.length[1]

    while i < len(events) and events[i][0] == x:
        _, typ, y1, y2 = events[i]
        tree.update(1, 0, tree.n, y_index[y1], y_index[y2], typ)
        i += 1

    prev_x = x

print(area)
