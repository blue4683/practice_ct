from collections import defaultdict
import sys
input = sys.stdin.readline
direction = [(-1, 0), (-1, 1), (0, 1), (1, 1),
             (1, 0), (1, -1), (0, -1), (-1, -1)]

n, m, k = map(int, input().split())
arr = defaultdict(list)
q = []
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    arr[(r - 1, c - 1)].append((m, s, d))
    q.append((r - 1, c - 1))

for _ in range(k):
    moved = []
    while q:
        y, x = q.pop()
        m, s, d = arr[(y, x)].pop()
        dy, dx = direction[d]
        yy, xx = (y + dy * s) % n, (x + dx * s) % n
        moved.append((yy, xx, m, s, d))

    for y, x, m, s, d in moved:
        arr[(y, x)].append((m, s, d))

    new_q = []
    for y, x in arr.keys():
        if not arr[(y, x)]:
            continue

        if len(arr[(y, x)]) > 1:
            m = sum([m for m, _, _ in arr[(y, x)]]) // 5
            if not m:
                arr[(y, x)] = []
                continue

            s = sum([s for _, s, _ in arr[(y, x)]]) // len(arr[(y, x)])
            if len(set(map(lambda x: x[2] % 2, arr[(y, x)]))) > 1:
                arr[(y, x)] = []
                for i in range(1, 8, 2):
                    arr[(y, x)].append((m, s, i))
                    new_q.append((y, x))

            else:
                arr[(y, x)] = []
                for i in range(0, 8, 2):
                    arr[(y, x)].append((m, s, i))
                    new_q.append((y, x))

        else:
            new_q.append((y, x))

    q = new_q[:]

result = 0
for y, x in arr.keys():
    for m, _, _ in arr[(y, x)]:
        result += m

print(result)
