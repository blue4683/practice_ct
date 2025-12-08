import sys
input = sys.stdin.readline


def compute_y_total():
    length = 0.0
    for i in range(len(active)):
        if active[i] > 0:
            length += ys[i + 1] - ys[i]

    return length


n = int(input())

rects = []
ys = set()
events = []
for _ in range(n):
    x, y, w, h = map(float, input().split())
    x1 = x
    x2 = x + w
    y1 = y
    y2 = y + h

    events.append((x1, 1, y1, y2))
    events.append((x2, -1, y1, y2))

    ys.add(y1)
    ys.add(y2)

ys = sorted(ys)
y_index = {v: i for i, v in enumerate(ys)}

active = [0] * (len(ys) - 1)
events.sort()

area = 0.0
prev_x = events[0][0]
prev_y_total = 0.0

for x, typ, y1, y2 in events:
    dx = x - prev_x
    area += dx * prev_y_total

    s = y_index[y1]
    e = y_index[y2]
    for i in range(s, e):
        active[i] += typ

    prev_x = x
    prev_y_total = compute_y_total()

if area.is_integer():
    print(int(area))

else:
    print(f"{area:.2f}")
